from utils import get_db_connection

def get_counts(conn):
    cur = conn.cursor()

    cur.execute("select count(*) from mprs_mpan")
    a1 = cur.fetchone()[0]

    cur.execute("select count(*) from mavis_mpan")
    a2 = cur.fetchone()[0]

    cur.execute("select count(*) from mprs_mpan where mpan is null or mpan_type is null")
    a3 = cur.fetchone()[0]

    cur.execute("select count(*) from mavis_mpan where mpan is null or mpan_type is null")
    a4 = cur.fetchone()[0]

    cur.close()
    return a1, a2, a3, a4

def test_row_count_match(log_result):
    conn = get_db_connection()
    try:
        a1, a2, _, _ = get_counts(conn)
        assert a1 == a2
        log_result("test_row_count_match", "PASS")
    except AssertionError as e:
        log_result("test_row_count_match", "FAIL", str(e))
        raise
    finally:
        conn.close()

def test_mavis_mpan_null_checks(log_result):
    conn = get_db_connection()
    try:
        _, _, a3, _ = get_counts(conn)
        assert a3 == 0
        log_result("test_mavis_mpan_null_checks", "PASS")
    except AssertionError:
        failure_msg = "Mavis table has NULL values in MPAN or MPAN_TYPE"
        log_result("test_mavis_mpan_null_checks", "FAIL", failure_msg)
        raise
    finally:
        conn.close()

def test_mprs_mpan_null_checks(log_result):
    conn = get_db_connection()
    try:
        _, _, _, a4 = get_counts(conn)
        assert a4 == 0
        log_result("test_mprs_mpan_null_checks", "PASS")
    except AssertionError as e:
        log_result("test_mprs_mpan_null_checks", "FAIL", str(e))
        raise
    finally:
        conn.close()