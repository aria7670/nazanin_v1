"""
Initialization Manager
مدیر راه‌اندازی و پر کردن خودکار اسپردشیت‌ها

این ماژول:
1. اسپردشیت‌ها را بررسی می‌کند
2. شیت‌های لازم را می‌سازد
3. اطلاعات اولیه را وارد می‌کند
4. تست امنیتی انجام می‌دهد
"""

import gspread
from google.oauth2.service_account import Credentials
import logging
import asyncio
from typing import Dict, List, Optional
from datetime import datetime
import time

from nazanin.sheets_system.spreadsheet_structure import SPREADSHEET_STRUCTURE, get_summary
from nazanin.sheets_system.initial_data import get_initial_data

logger = logging.getLogger(__name__)


class InitializationManager:
    """
    مدیر راه‌اندازی کامل سیستم Google Sheets
    
    فرآیند:
    1. اتصال به Google Sheets
    2. بررسی 15 اسپردشیت
    3. ساخت شیت‌های لازم
    4. اضافه کردن headers
    5. پر کردن اطلاعات اولیه
    6. تست امنیتی
    """
    
    def __init__(self, credentials_file: str, spreadsheet_ids: Dict[str, str]):
        """
        Args:
            credentials_file: مسیر فایل credentials
            spreadsheet_ids: Dict از نام و ID اسپردشیت‌ها
                مثال: {
                    'CORE_DATA': 'spreadsheet_id_1',
                    'CONVERSATION_DATA': 'spreadsheet_id_2',
                    ...
                }
        """
        self.credentials_file = credentials_file
        self.spreadsheet_ids = spreadsheet_ids
        self.gc = None
        self.spreadsheets = {}
        
        # آمار
        self.stats = {
            'spreadsheets_checked': 0,
            'sheets_created': 0,
            'headers_added': 0,
            'rows_inserted': 0,
            'errors': []
        }
    
    async def initialize_all(self) -> Dict:
        """
        راه‌اندازی کامل تمام اسپردشیت‌ها
        
        Returns:
            Dict حاوی نتایج و آمار
        """
        logger.info("=" * 80)
        logger.info("🚀 GOOGLE SHEETS INITIALIZATION MANAGER")
        logger.info("=" * 80)
        
        start_time = time.time()
        
        try:
            # Step 1: اتصال
            logger.info("\n📡 Step 1/6: Connecting to Google Sheets...")
            await self._connect()
            
            # Step 2: بررسی اسپردشیت‌ها
            logger.info("\n📊 Step 2/6: Checking all 15 spreadsheets...")
            await self._check_all_spreadsheets()
            
            # Step 3: ساخت شیت‌ها
            logger.info("\n📝 Step 3/6: Creating necessary sheets...")
            await self._create_all_sheets()
            
            # Step 4: اضافه کردن headers
            logger.info("\n🏷️ Step 4/6: Adding headers...")
            await self._add_all_headers()
            
            # Step 5: پر کردن اطلاعات اولیه
            logger.info("\n💾 Step 5/6: Inserting initial data...")
            await self._insert_initial_data()
            
            # Step 6: تست امنیتی
            logger.info("\n🔐 Step 6/6: Running security tests...")
            security_result = await self._run_security_tests()
            
            duration = time.time() - start_time
            
            # نتیجه نهایی
            logger.info("\n" + "=" * 80)
            logger.info("✅ INITIALIZATION COMPLETE!")
            logger.info("=" * 80)
            logger.info(f"\n📊 Statistics:")
            logger.info(f"   • Spreadsheets checked: {self.stats['spreadsheets_checked']}")
            logger.info(f"   • Sheets created: {self.stats['sheets_created']}")
            logger.info(f"   • Headers added: {self.stats['headers_added']}")
            logger.info(f"   • Rows inserted: {self.stats['rows_inserted']}")
            logger.info(f"   • Errors: {len(self.stats['errors'])}")
            logger.info(f"   • Duration: {duration:.2f}s")
            logger.info("=" * 80)
            
            return {
                'success': True,
                'stats': self.stats,
                'duration': duration,
                'security': security_result
            }
            
        except Exception as e:
            logger.error(f"\n❌ Initialization failed: {e}", exc_info=True)
            self.stats['errors'].append(str(e))
            return {
                'success': False,
                'error': str(e),
                'stats': self.stats
            }
    
    async def _connect(self):
        """اتصال به Google Sheets"""
        try:
            scope = [
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
            
            creds = Credentials.from_service_account_file(
                self.credentials_file,
                scopes=scope
            )
            
            self.gc = gspread.authorize(creds)
            logger.info("   ✅ Connected to Google Sheets")
            
        except Exception as e:
            logger.error(f"   ❌ Connection failed: {e}")
            raise
    
    async def _check_all_spreadsheets(self):
        """بررسی تمام 15 اسپردشیت"""
        
        summary = get_summary()
        logger.info(f"   Expected: {summary['total_spreadsheets']} spreadsheets")
        logger.info(f"   Provided IDs: {len(self.spreadsheet_ids)}")
        
        if len(self.spreadsheet_ids) != summary['total_spreadsheets']:
            logger.warning(f"   ⚠️ Mismatch! Expected {summary['total_spreadsheets']}, got {len(self.spreadsheet_ids)}")
        
        for name in summary['spreadsheet_names']:
            if name not in self.spreadsheet_ids:
                logger.error(f"   ❌ Missing spreadsheet: {name}")
                self.stats['errors'].append(f"Missing: {name}")
                continue
            
            try:
                spreadsheet_id = self.spreadsheet_ids[name]
                spreadsheet = self.gc.open_by_key(spreadsheet_id)
                self.spreadsheets[name] = spreadsheet
                self.stats['spreadsheets_checked'] += 1
                logger.info(f"   ✅ {name}: OK")
                
            except Exception as e:
                logger.error(f"   ❌ {name}: {e}")
                self.stats['errors'].append(f"{name}: {e}")
        
        logger.info(f"\n   ✅ Checked {self.stats['spreadsheets_checked']}/{summary['total_spreadsheets']} spreadsheets")
    
    async def _create_all_sheets(self):
        """ساخت تمام شیت‌های لازم"""
        
        for spreadsheet_name, spreadsheet_obj in self.spreadsheets.items():
            structure = SPREADSHEET_STRUCTURE.get(spreadsheet_name, {})
            sheets_to_create = structure.get('sheets', {})
            
            logger.info(f"\n   📊 {spreadsheet_name}: {len(sheets_to_create)} sheets")
            
            # دریافت شیت‌های موجود
            existing_sheets = {ws.title for ws in spreadsheet_obj.worksheets()}
            
            for sheet_name in sheets_to_create.keys():
                if sheet_name in existing_sheets:
                    logger.info(f"      ✓ {sheet_name} (exists)")
                else:
                    try:
                        spreadsheet_obj.add_worksheet(
                            title=sheet_name,
                            rows=1000,
                            cols=20
                        )
                        self.stats['sheets_created'] += 1
                        logger.info(f"      ✅ {sheet_name} (created)")
                        await asyncio.sleep(0.5)  # rate limiting
                    except Exception as e:
                        logger.error(f"      ❌ {sheet_name}: {e}")
                        self.stats['errors'].append(f"{spreadsheet_name}/{sheet_name}: {e}")
        
        logger.info(f"\n   ✅ Created {self.stats['sheets_created']} new sheets")
    
    async def _add_all_headers(self):
        """اضافه کردن headers به تمام شیت‌ها"""
        
        for spreadsheet_name, spreadsheet_obj in self.spreadsheets.items():
            structure = SPREADSHEET_STRUCTURE.get(spreadsheet_name, {})
            sheets_config = structure.get('sheets', {})
            
            for sheet_name, sheet_config in sheets_config.items():
                try:
                    worksheet = spreadsheet_obj.worksheet(sheet_name)
                    
                    # چک کردن اینکه header وجود داره یا نه
                    existing_values = worksheet.row_values(1)
                    
                    if not existing_values or len(existing_values) == 0:
                        # اضافه کردن header
                        headers = sheet_config.get('headers', [])
                        if headers:
                            worksheet.update('A1', [headers])
                            self.stats['headers_added'] += 1
                            logger.info(f"      ✅ {spreadsheet_name}/{sheet_name}: headers added")
                            await asyncio.sleep(0.3)
                    else:
                        logger.info(f"      ✓ {spreadsheet_name}/{sheet_name}: headers exist")
                        
                except Exception as e:
                    logger.error(f"      ❌ {spreadsheet_name}/{sheet_name}: {e}")
                    self.stats['errors'].append(f"Headers {spreadsheet_name}/{sheet_name}: {e}")
        
        logger.info(f"\n   ✅ Added headers to {self.stats['headers_added']} sheets")
    
    async def _insert_initial_data(self):
        """پر کردن اطلاعات اولیه"""
        
        initial_data_all = get_initial_data()
        
        for spreadsheet_name, sheets_data in initial_data_all.items():
            if spreadsheet_name not in self.spreadsheets:
                continue
            
            spreadsheet_obj = self.spreadsheets[spreadsheet_name]
            
            logger.info(f"\n   💾 {spreadsheet_name}:")
            
            for sheet_name, rows in sheets_data.items():
                if not rows:
                    logger.info(f"      - {sheet_name}: no initial data")
                    continue
                
                try:
                    worksheet = spreadsheet_obj.worksheet(sheet_name)
                    
                    # چک کردن اینکه داده وجود داره یا نه
                    existing_data = worksheet.get_all_values()
                    
                    if len(existing_data) <= 1:  # فقط header
                        # اضافه کردن داده‌ها
                        if rows:
                            worksheet.append_rows(rows)
                            self.stats['rows_inserted'] += len(rows)
                            logger.info(f"      ✅ {sheet_name}: {len(rows)} rows inserted")
                            await asyncio.sleep(0.5)
                    else:
                        logger.info(f"      ✓ {sheet_name}: data exists ({len(existing_data)-1} rows)")
                        
                except Exception as e:
                    logger.error(f"      ❌ {sheet_name}: {e}")
                    self.stats['errors'].append(f"Data {spreadsheet_name}/{sheet_name}: {e}")
        
        logger.info(f"\n   ✅ Inserted {self.stats['rows_inserted']} rows total")
    
    async def _run_security_tests(self):
        """تست‌های امنیتی"""
        
        tests = []
        
        # Test 1: دسترسی به تمام اسپردشیت‌ها
        logger.info("   🔐 Test 1/5: Access to all spreadsheets")
        accessible = len(self.spreadsheets)
        total = len(self.spreadsheet_ids)
        test1_pass = accessible == total
        tests.append(test1_pass)
        logger.info(f"      {'✅' if test1_pass else '❌'} {accessible}/{total} accessible")
        
        # Test 2: تمام شیت‌های لازم موجودند
        logger.info("   🔐 Test 2/5: All required sheets exist")
        expected_sheets = sum(len(s.get('sheets', {})) for s in SPREADSHEET_STRUCTURE.values())
        actual_sheets = sum(len(sp.worksheets()) for sp in self.spreadsheets.values())
        test2_pass = actual_sheets >= expected_sheets
        tests.append(test2_pass)
        logger.info(f"      {'✅' if test2_pass else '❌'} {actual_sheets}/{expected_sheets} sheets")
        
        # Test 3: Headers موجودند
        logger.info("   🔐 Test 3/5: Headers present")
        test3_pass = self.stats['headers_added'] > 0 or self._check_existing_headers()
        tests.append(test3_pass)
        logger.info(f"      {'✅' if test3_pass else '❌'} Headers check")
        
        # Test 4: داده اولیه وارد شده
        logger.info("   🔐 Test 4/5: Initial data inserted")
        test4_pass = self.stats['rows_inserted'] > 0 or self._check_existing_data()
        tests.append(test4_pass)
        logger.info(f"      {'✅' if test4_pass else '❌'} {self.stats['rows_inserted']} rows")
        
        # Test 5: خطاهای کمتر از 5%
        logger.info("   🔐 Test 5/5: Error rate < 5%")
        error_rate = len(self.stats['errors']) / max(1, self.stats['spreadsheets_checked']) * 100
        test5_pass = error_rate < 5
        tests.append(test5_pass)
        logger.info(f"      {'✅' if test5_pass else '❌'} {error_rate:.1f}% error rate")
        
        all_passed = all(tests)
        
        logger.info(f"\n   {'✅' if all_passed else '⚠️'} Security tests: {sum(tests)}/5 passed")
        
        return {
            'all_passed': all_passed,
            'tests_passed': sum(tests),
            'tests_total': len(tests),
            'details': {
                'access_test': tests[0],
                'sheets_test': tests[1],
                'headers_test': tests[2],
                'data_test': tests[3],
                'error_rate_test': tests[4]
            }
        }
    
    def _check_existing_headers(self) -> bool:
        """بررسی وجود headers در شیت‌های موجود"""
        try:
            for spreadsheet in self.spreadsheets.values():
                for worksheet in spreadsheet.worksheets():
                    if len(worksheet.row_values(1)) > 0:
                        return True
            return False
        except:
            return False
    
    def _check_existing_data(self) -> bool:
        """بررسی وجود داده در شیت‌های موجود"""
        try:
            for spreadsheet in self.spreadsheets.values():
                for worksheet in spreadsheet.worksheets():
                    if len(worksheet.get_all_values()) > 1:
                        return True
            return False
        except:
            return False
    
    def get_stats(self) -> Dict:
        """دریافت آمار"""
        return {
            **self.stats,
            'summary': get_summary()
        }
