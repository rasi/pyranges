
import pytest
from tests.helpers import assert_df_equal

from pyranges.pyranges import PyRanges
import pyranges as pr

import pandas as pd

from io import StringIO

@pytest.fixture
def expected_result_unstranded():

 c = """Chromosome Start End Name Score Strand Chromosome_b Start_b End_b Name_b Score_b Strand_b Distance
chr1 9916 10115 HWI-ST216_313:3:1203:10227:6568 1 - chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 9939 10138 HWI-ST216_313:3:2301:15791:16298 1 + chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 9951 10150 HWI-ST216_313:3:2205:20086:33508 1 - chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 9953 10152 HWI-ST216_313:3:1305:6975:102491 1 + chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 9978 10177 HWI-ST216_313:3:1204:5599:113305 1 - chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 10001 10200 HWI-ST216_313:3:1102:14019:151362 1 - chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 10024 10223 HWI-ST216_313:3:2201:5209:155139 1 + chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 10127 10326 HWI-ST216_313:3:2207:7406:122346 1 - chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 10241 10440 HWI-ST216_313:3:1302:4516:156396 1 - chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 10246 10445 HWI-ST216_313:3:1207:4315:142177 1 + chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 110246 110445 HWI-ST216_313:3:1207:4315:142177 1 + chr1 19958 20157 HWI-ST216:427:D29R1ACXX:2:1313:6283:67310 1 - 90089"""

 return PyRanges(pd.read_table(StringIO(c), sep=" "))


def test_nearest_bed_unstranded(chip_10_plus_one, input_10, expected_result_unstranded):

    result = chip_10_plus_one.nearest(input_10, strandedness=False, suffix="_b")

    print(result.df.to_csv(sep=" "))

    assert assert_df_equal(result.df, expected_result_unstranded.df)



@pytest.fixture
def expected_result_same_stranded():

    c = """Chromosome Start End Name Score Strand Chromosome_b Start_b End_b Name_b Score_b Strand_b Distance
chr1 9939 10138 HWI-ST216_313:3:2301:15791:16298 1 + chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 9953 10152 HWI-ST216_313:3:1305:6975:102491 1 + chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 10024 10223 HWI-ST216_313:3:2201:5209:155139 1 + chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 10246 10445 HWI-ST216_313:3:1207:4315:142177 1 + chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 110246 110445 HWI-ST216_313:3:1207:4315:142177 1 + chr1 16109 16308 HWI-ST216:427:D29R1ACXX:2:2110:12286:25379 1 + 93938
chr1 9916 10115 HWI-ST216_313:3:1203:10227:6568 1 - chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 9951 10150 HWI-ST216_313:3:2205:20086:33508 1 - chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 9978 10177 HWI-ST216_313:3:1204:5599:113305 1 - chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 10001 10200 HWI-ST216_313:3:1102:14019:151362 1 - chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 10127 10326 HWI-ST216_313:3:2207:7406:122346 1 - chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 10241 10440 HWI-ST216_313:3:1302:4516:156396 1 - chr1 10079 10278 HWI-ST216:427:D29R1ACXX:2:1314:10333:38924 1 - 0"""

    return PyRanges(pd.read_table(StringIO(c), sep=" "))


def test_nearest_bed_same_stranded(chip_10_plus_one, input_10, expected_result_same_stranded):

    result = chip_10_plus_one.nearest(input_10, strandedness="same", suffix="_b")

    print(result.df.to_csv(sep=" "))

    assert assert_df_equal(result.df, expected_result_same_stranded.df)


@pytest.fixture
def expected_result_opposite_stranded():

    c = """Chromosome Start End Name Score Strand Chromosome_b Start_b End_b Name_b Score_b Strand_b Distance
chr1 9939 10138 HWI-ST216_313:3:2301:15791:16298 1 + chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 9953 10152 HWI-ST216_313:3:1305:6975:102491 1 + chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 10024 10223 HWI-ST216_313:3:2201:5209:155139 1 + chr1 9988 10187 HWI-ST216:427:D29R1ACXX:2:1205:6095:16532 1 - 0
chr1 10246 10445 HWI-ST216_313:3:1207:4315:142177 1 + chr1 10079 10278 HWI-ST216:427:D29R1ACXX:2:1314:10333:38924 1 - 0
chr1 110246 110445 HWI-ST216_313:3:1207:4315:142177 1 + chr1 19958 20157 HWI-ST216:427:D29R1ACXX:2:1313:6283:67310 1 - 90089
chr1 9916 10115 HWI-ST216_313:3:1203:10227:6568 1 - chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 9951 10150 HWI-ST216_313:3:2205:20086:33508 1 - chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 9978 10177 HWI-ST216_313:3:1204:5599:113305 1 - chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 10001 10200 HWI-ST216_313:3:1102:14019:151362 1 - chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 10127 10326 HWI-ST216_313:3:2207:7406:122346 1 - chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0
chr1 10241 10440 HWI-ST216_313:3:1302:4516:156396 1 - chr1 10073 10272 HWI-ST216:427:D29R1ACXX:2:2302:14161:85418 1 + 0"""

    return PyRanges(pd.read_table(StringIO(c), sep=" "))


def test_nearest_bed_opposite_stranded(chip_10_plus_one, input_10, expected_result_opposite_stranded):

    result = chip_10_plus_one.nearest(input_10, strandedness="opposite", suffix="_b")

    print(result.df.to_csv(sep=" "))

    assert assert_df_equal(result.df, expected_result_opposite_stranded.df)