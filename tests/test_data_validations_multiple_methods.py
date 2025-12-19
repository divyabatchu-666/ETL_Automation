import oracledb
import pandas as pd

def get_counts():
    conn = oracledb.connect("oracle/oracle@localhost:1521/")
    cur = conn.cursor()

    # count validation between Mprs_mpan & Mavis_mpan tables
    cur.execute("select count(*) from mprs_mpan")
    a1 = cur.fetchone()[0]

    cur.execute("select count(*) from mavis_mpan")
    a2 = cur.fetchone()[0]

    # count validation between Mprs_mpan & Mavis_mpan tables
    cur.execute("select count(*) from mprs_mpan where mpan is null or mpan_type is null")
    a3 = cur.fetchone()[0]

    cur.execute("select count(*) from mavis_mpan where mpan is null or mpan_type is null")
    a4 = cur.fetchone()[0]

    cur.close()
    conn.close()
    return a1,a2,a3,a4

def test_row_count_match():
    a1,a2,_,_=get_counts()
    assert a1==a2,f"Row count mismatch: {a1} vs {a2}"

def test_mavis_mpan_no_nulls():
    _,_,a3,_= get_counts()
    assert a3==0, f"Mavis_Mpan table has null values in MPAN & MPAN_type columns : {a3}"

def test_mprs_mpan_no_nulls():
    _,_,_,a4= get_counts()
    assert a4==0, f"Mprs_Mpan table has null values in MPAN & MPAN_type columns : {a4}"

