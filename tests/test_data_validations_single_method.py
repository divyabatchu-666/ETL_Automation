import oracledb
import pandas as pd

def test_data_validations():
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

    assert a1==a2,f"Row count mismatch: {a1} vs {a2}"
    assert a3==0, f"Mavis_Mpan table has null values in MPAN & MPAN_type columns : {a3}"
    assert a4==0, f"Mprs_Mpan table has null values in MPAN & MPAN_type columns : {a4}"

