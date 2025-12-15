import oracledb
import pandas as pd

def test_emp_validations():
    conn = oracledb.connect("oracle/oracle@localhost:1521/")
    cur = conn.cursor()

    # Total employees
    cur.execute("select count(*) from emp")
    total_count = cur.fetchone()[0]

    # Employees in dept 30
    cur.execute("select count(*) from emp where deptno = 30")
    dept30_count = cur.fetchone()[0]

    # Invalid departments
    cur.execute("select count(*), deptno from emp where deptno not in (10,20,30,40) group by deptno")
    invalid_depts = cur.fetchall()

    # Employee details
    cur.execute("select * from emp")
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]
    df_emp = pd.DataFrame(rows, columns=columns)

    # ================== ASSERTIONS (Jenkins cares about these) ==================

    assert total_count > 0, "EMP table is empty"
    assert dept30_count >= 0, "Dept 30 count validation failed"
    assert len(invalid_depts) == 0, "Invalid department data found"
    assert not df_emp.empty, "Employee table returned no records"

    # ================== LOG OUTPUT (for Jenkins console) ==================

    print("\nTotal Employee count:", total_count)
    print("Employees in Dept 30:", dept30_count)
    print("Invalid department records (should be empty):", invalid_depts)
    print("\nEmployee details:\n", df_emp.to_string(index=False))

    conn.close()
