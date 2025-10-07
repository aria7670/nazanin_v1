"""
Biological System
سیستم بیولوژیکی - شبیه‌سازی بدن انسان
"""

from nazanin.bio_system.cell_system import Cell, Tissue, Organ, Brain, Heart, Lungs
from nazanin.bio_system.body_systems import (
    BodySystem,
    NervousSystem,
    CirculatorySystem,
    RespiratorySystem,
    DigestiveSystem,
    ImmuneSystem,
    EndocrineSystem,
    MusculoskeletalSystem,
    Organism
)

__all__ = [
    'Cell',
    'Tissue',
    'Organ',
    'Brain',
    'Heart',
    'Lungs',
    'BodySystem',
    'NervousSystem',
    'CirculatorySystem',
    'RespiratorySystem',
    'DigestiveSystem',
    'ImmuneSystem',
    'EndocrineSystem',
    'MusculoskeletalSystem',
    'Organism'
]
