import database,sys

def menu(cnx):
    opcion = 0
    print("1. Lista la información de los empleados en el que las fechas aparezcan en formato dd/mm/yyyy \n"+
    "2. Lista nombre, apellidos y salario de los empleados \n"+
    "3. Lista nombre, apellidos y departamento al que pertenecen los empleados \n"+
    "4. Lista nombre, apellidos y títulos que ostenta cada uno de los empleados \n"+
    "5. Lista los empleados con fecha de contratación posterior a 22 de febrero de 1991 \n"+
    "6. Crea un nuevo empleado al que le pidas: nombre, apellidos, género y fecha de nacimiento"+
    "7. Actualiza el salario del último empleado dado de alta a 45.000 \n"+
    "8. Borra toda la información relacionada con un empleado \n"+
    "9. Salir")
    opcion = int(input('Introduce un número : '))
    opciones = {'1': ej1,'2' : ej2,'3' : ej3, '4' : ej4, '5' : ej5, '6' : ej6, '7' : ej7, '8' : ej8}
    while opcion != 9:
        opciones[str(opcion)](cnx)
        menu(cnx)
    sys.exit()
        

def ej1(cnx):
    cursor = cnx.cursor()

    query=("SELECT first_name, last_name, DATE_FORMAT(birth_date,'%d/%m/%Y'), gender, DATE_FORMAT(hire_date,'%d/%m/%Y') FROM employees")

    cursor.execute(query)
    
    for (first_name, last_name, birth_date, gender, hire_date) in cursor:
        print(first_name, last_name, birth_date, gender, hire_date)
    
    database.close_db(cnx)

def ej2(cnx):
    cursor = cnx.cursor()

    query=("SELECT e.first_name,e.last_name,GROUP_CONCAT(s.salary) "+
    "FROM employees e "+
    "INNER JOIN salaries s ON e.emp_no = s.emp_no "+
    "GROUP BY e.emp_no;")

    cursor.execute(query)
    for (first_name, last_name, salary) in cursor:
        print(first_name, last_name, salary)

def ej3(cnx):
    cursor = cnx.cursor()

    query=("SELECT e.first_name,e.last_name,de.dept_name "+
    " FROM employees e "+
    " INNER JOIN dept_emp d ON e.emp_no = d.emp_no "+
    " INNER JOIN departments de ON de.dept_no = d.dept_no;")

    cursor.execute(query)
    for (first_name, last_name, dept_no) in cursor:
        print(first_name, last_name, dept_no)

def ej4(cnx):
    cursor = cnx.cursor()

    query=("SELECT e.first_name,e.last_name,GROUP_CONCAT(t.title) "+
    " FROM employees e "+
    " INNER JOIN titles t ON e.emp_no = t.emp_no "+
    " GROUP BY e.emp_no;")

    cursor.execute(query)
    for (first_name, last_name, title) in cursor:
        print(first_name, last_name, title)


def ej5(cnx):
    cursor = cnx.cursor()

    query=("SELECT e.first_name,e.last_name,GROUP_CONCAT(s.salary), e.hire_date"+
    " FROM employees e "+
    " INNER JOIN salaries s ON e.emp_no = s.emp_no "+
    " WHERE e.hire_date > '1991-02-22' "+
    " GROUP BY e.emp_no;")

    cursor.execute(query)
    for (first_name, last_name, salary,hire_date) in cursor:
        print(first_name, last_name, salary,hire_date)


def ej6(cnx):
    

    nombre = str(input('Introduce el nombre del empleado : '))
    apellidos = str(input('Introduce los apellidos : '))
    genero = str(input('Introduce el género : '))
    fecha_nac = str(input('Introduce la fecha de nacimiento : '))
    add_employee = ("INSERT INTO employees "+
    " (first_name, last_name, hire_date, gender,birth_date) "+
    " VALUES (%s, %s, %s, %s, %s)")
    add_salary = ("INSERT INTO salaries "+
    " (salary, from_date) "+
    " VALUES (%(salary)s, %(from_date)s)")

    data_employee = (nombre, apellidos, getdate(), 'M', date(1977,
    6, 14))

    

def ej7(cnx):
    print("hola")

def ej8(cnx):
    print("hola")

if __name__ == '__main__':
    cnx = database.connect_db()
    menu(cnx)
