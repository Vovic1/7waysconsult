from type_lib import poll
import json
import pyodbc

def get_row(r: []):
    return {
        'id': r[0],
        'name': r[1],
        'descr': r[2],
        'is_act': r[3],
        'is_del': r[4]
    }       



#cs = "Data Source=V500GB\\SQLEXPRESS;Initial Catalog=CInfo;Integrated Security=True"
cs = "Driver={ODBC Driver 17 for SQL Server};Server=localhost\SQLEXPRESS;Database=CInfo;Trusted_Connection=yes;"

#con = pyodbc.connect(cs)
#cursor = con.cursor()
#cursor.execute('SELECT * FROM employee_db')
#for row in cursor:
#    print('row = %r' % (row,))

def poll_add(p: poll):
    print("name = %s , descr = %s..." % (p.name, p.descr))
    con = pyodbc.connect(cs)
    c = con.cursor()
    c.execute('INSERT INTO polls VALUES (?, ?, ?, ?)', p.name, p.descr, p.is_act, p.is_del)
    con.commit()
    c.execute('SELECT TOP 1 id FROM polls ORDER BY ID DESC')
    r = c.fetchone()
    #id = r[0]
    #print("id = %i" % id)
    con.close()
    return get_row(r)  #json.dumps(r)     #id # {"id": id}

def poll_upd(id:int, p: poll):
    print("poll_upd >> id = %i, name = %s , descr = %s..." % (p.id, p.name, p.descr))
    con = pyodbc.connect(cs)
    try:
        c = con.cursor()  
        c.execute('UPDATE polls SET name=?, descr=?, is_act=?, is_del=? WHERE id=?', p.name, p.descr, p.is_act, p.is_del, id)
        con.commit()
        con.close()
        return json.dump(vars(p))
    except:
        con.close()
        return {"status": "Error"}

def poll_status(id:int, b:bool):
    con = pyodbc.connect(cs)
    try:
        c = con.cursor()
        c.execute('UPDATE polls SET is_act=? WHERE id=?', b, id)
        con.commit()
        con.close()
        return {"status": "Ok"}
    except:
        con.close()
        return  {"status": "Error"} 

def poll_by_id(id:int):
    con = pyodbc.connect(cs)
    c = con.cursor()
    c.execute('SELECT top 1 * FROM polls WHERE id=?', id)
    r = c.fetchone()
    #rid = c.row[0]
    con.close()
    return get_row(r)   #json.dumps(r)

def poll_table():
    con = pyodbc.connect(cs)
    c = con.cursor()
    #c.execute('SELECT id, name, descr, is_act, is_del FROM polls')
    c.execute('SELECT id, name, descr, is_act, is_del FROM polls WHERE is_act=1 and is_del=0')
    polls = []
    
    for r in c:
        row = {
            'id': r[0],         #.get('id'),
            'name': r[1],       #.get('name'),
            'descr': r[2],      #.get('descr'),
            'is_act': r[3],     #.get('is_act'),
            'is_del': r[4]      #.get('is_del')
        }       
        polls.append(row)
        #polls.append(json.dumps(r))

    con.close()
    return polls


