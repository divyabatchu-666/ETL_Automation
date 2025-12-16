import oracledb
import pandas as pd

def test_select_from_customer():
    conn = oracledb.connect("oracle/oracle@localhost:1521/")
    cur = conn.cursor()

    # Total employees
    cur.execute("select count(*) from emp")
    a1 = cur.fetchone()[0]

    # Employees in dept 30
    cur.execute("select count(*) from emp where deptno = 50")
    a2 = cur.fetchone()[0]

    # Invalid departments check
    cur.execute("select count(*), deptno from emp where deptno not in (10,20,30,40) group by deptno")
    a3 = cur.fetchall()

    # Employee details
    cur.execute("select * from emp")
    a4 = cur.fetchall()
    columns = [col[0] for col in cur.description]
    df2 = pd.DataFrame(a4, columns=columns)

    # Output
    if a1> 0: # a2 output displays in integer itself so not need to define it in len()
        print("\nEmployee count in EMP table:", a1)
    else:
        print("\nEmployee count in EMP table:", "No data exist in EMP table")


    if a2>0: # a2 output displays in integer itself so not need to define it in len()
        print("\nEmployee count under deptno=30:", a2)
    else:
        print("\nEmployee count under deptno=50:", "No data exist")

    if len(a3)>0: # table data displays in list, tuple ,dictionary so we need to dine it as len()
        print("\nEmployee count under each department:", a3)
    else:
        print("\nEmployee count under each department:", "No department data found")


    if len(a4) > 0: # table data displays in list, tuple ,dictionary so we need to dine it as len()
        print("\nEmployee details under EMP table:\n", df2.to_string(index=False))
    else:
        print("\nEmployee details under EMP table:", "No data exist in EMP table")

    conn.close()
