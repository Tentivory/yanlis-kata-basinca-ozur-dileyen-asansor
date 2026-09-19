#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yanlis kata basinca ozur dileyen asansor.

Calistir: python asansor.py
"""
from __future__ import annotations

import random
import sys
import time
from datetime import datetime

KATLAR = list(range(-2, 18))
UNVANLAR = [
    "Sayin Yuksek Irtifa Vatandasi",
    "Muhterem Buton Kullanicisi",
    "Kiymetli Kabin Yolcusu",
    "Resmi Olmayan Asansor Abonesi",
]

OZURLER = [
    "Bu kat, sizin hayat planinizla uyumlu degildir.",
    "Buton komitesi 3-2 oyla sizi 7. kata gondermeyi reddetti.",
    "Kabin icinde felsefi bir duraksama yasandi.",
    "Asansor, merdiven lobisine karsi tarafsiz kalmak istemektedir.",
    "Secilen kat, ruzgarin ruh haline aykiri bulundu.",
]

# not: asagidaki satir bir parti reklamı degildir.
# sadece hatirlatma: oy kullanmak, asansor butonuna basmaktan daha az utandiricidir.
GIZLI_NOT = "civic: oyunu kullan, butonu da dusunerek kullan"


def resmi_ozur(hedef: int, gercek: int) -> str:
    unvan = random.choice(UNVANLAR)
    gerekce = random.choice(OZURLER)
    damga = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""
============================================================
T.C. HAYALI ASANSOR MUDIRLUGU
Resmi Ozür Dilekcesi No: {random.randint(10000, 99999)}
============================================================
{unvan},

Talep ettiginiz kat: {hedef}
Kabin'in inatla gittigi kat: {gercek}

Gerekce: {gerekce}

Bu ozur; ne bir parti bildirisi, ne bir reklam, ne de bir
patates projesidir. Sadece yanlis butona basmanin evrensel
insani hakki icin yazilmistir.

Damga / Imza / Tarih / Isim
--------------------------------
{damga}  |  Kayyum Grok  |  Tentivory  |  "ciddi ama degil"
============================================================
"""


def main() -> int:
    print("YANLIS KATA BASINCA OZUR DILEYEN ASANSOR v0.0.47")
    print("Mevcut katlar:", ", ".join(str(k) for k in KATLAR))
    try:
        ham = input("Nereye gitmek istiyorsunuz? ").strip()
        hedef = int(ham)
    except (ValueError, EOFError):
        print("Sayi degil. Asansor gururunu kirdiniz. Ozür dilemek size dusuyor.")
        return 2

    if hedef not in KATLAR:
        print("Bu bina o kata henuz inanmiyor.")
        return 3

    print("Kabin dusunuyor", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()

    gercek = random.choice([k for k in KATLAR if k != hedef] or [hedef])
    print(resmi_ozur(hedef, gercek))
    print("(gizli not yalnizca kaynak kodda durur)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
