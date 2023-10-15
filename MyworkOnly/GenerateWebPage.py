import sqlite3
import mysql.connector
import psycopg2
import os
# i need to change the way of taking input by using the code below
#<input type="number" id="quantity" name="quantity" min=1>
#<input type="date" name="StartDate" class=" form-control" id="StartDate" placeholder="Start Date">

# Sqlite and mysql generatig are working perfectly.
# PostgreSQL and sqlite we need the types of columns to know when should use single or double cotations.
# since a string only use single cotation
# for Database name and columns name use double cotations
# add function only needs the type of column to be complete
# Delete and save changes functions needs the column type and if statement for the new syntax of postgre
# like in add function.

# i need to create a select design page.
# make sure that the pages choose their style correctly.

#echo '<meta http-equiv="refresh" content="0; URL=Copy.php" />';


#for sqlite
DBName = "project.db"

def columns(tables):
    if(sqlite3.connect(DBName)):
        result = []
        conn = sqlite3.connect(DBName)
        cur = conn.cursor()
        l = len(tables)
        for m in range(l):
            cur.execute("PRAGMA table_info('"+tables[m]+"');")
            schema = cur.fetchall()
            x = len(schema)
            for i in range(x):
                sum =[]
                sum.append(m)
                sum.append(schema[i][1])  # Name
                sum.append(schema[i][5])  # PK?
                sum.append(schema[i][2])  #Type
                result.append(sum)

        conn.close()
        return result
    else:
        print("Failed")


def tables():
    if (sqlite3.connect(DBName)):
        result = []
        conn = sqlite3.connect(DBName)
        cur = conn.cursor()
        cur.execute('''SELECT name, sql FROM sqlite_master
                        WHERE type='table'
                        ORDER BY name;''')
        schema = cur.fetchall()

        x = len(schema)
        for i in range(x):
            result.append(schema[i][0])
        conn.close()
        return result
    else:
        print("Failed")


def PostgreTable():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="murtada2sayed",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        # print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        record = cursor.fetchall()
        result =[]
        x = len(record)
        for i in range(x):
            result.append(record[i][0])
        return result

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def PostgreColumns(tables):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="murtada2sayed",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        # print(connection.get_dsn_parameters(), "\n")
        # Print PostgreSQL version
        result = []
        PrimaryKey= ""
        l = len(tables)
        for m in range(l):#SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'some_table';
            # print(tables[m])
            cursor.execute("SELECT constraint_name, table_name, column_name FROM information_schema.key_column_usage"
                           +" WHERE table_name = '"+tables[m]+"';")# 0 = constraint, 1 table name, 2 =column name
            record = cursor.fetchall()
            # print("Primary key", record[0][0])
            if(record[0][0] == record[0][1]+"_pkey"):
                PrimaryKey = record[0][2]

            cursor.execute("SELECT column_name, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '"+tables[m]+"';")
            record = cursor.fetchall()
            x = len(record)
            for i in range(x):
                sum=[]
                sum.append(m)
                sum.append(record[i][0])
                if(record[i][0] == PrimaryKey):
                    sum.append(1)
                else:
                    sum.append(0)
                sum.append(record[i][1])
                result.append(sum)
            print("table Columns- ", *record, "\n")
        return result

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def MySQLTables(dbname):
    result=[]
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database=dbname
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = '"+dbname+"';")

    myresult = mycursor.fetchall()

    for x in myresult:
        result.append(x[0])
    return result

def MySQLColumns(tables, dbname):
    result = []
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database=dbname
    )

    mycursor = mydb.cursor()
    l = len(tables)
    for i in range(l):
        mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '"
                         +dbname+"' AND TABLE_NAME = '"+tables[i]+"' AND COLUMN_KEY = 'PRI';")
        # SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`. `COLUMNS` WHERE `TABLE_SCHEMA` = 'yourdatabasename' AND `TABLE_NAME` = 'yourtablename';
        myresult = mycursor.fetchall()
        PK = myresult[0][0]
        mycursor.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '"
                         + dbname + "' AND TABLE_NAME = '" + tables[i] + "';")
        myresult = mycursor.fetchall()
        for x in myresult:
            sum=[]
            sum.append(i)
            sum.append(x[0])
            if(x[0] == PK):
                sum.append(1)
            else:
                sum.append(0)
            sum.append(x[1])
            result.append(sum)
    return result


def beforeHTML(userID,wantedtables, filename, dbtype="sqlite"):
    tableslength = len(wantedtables)
    f = open(filename + ".php", "a+")
    f.write("<?php \n")  # done
    f.write("session_start();\n")
    f.write("if(empty($_SESSION['user'])){\n")
    f.write("   $_SESSION['user']='" + str(userID) + "';\n")
    f.write("}\n")
    if (dbtype != "sqlite"):
        f.write(
            "if (!empty($_SESSION['" + filename + "HostDB']) && !empty($_SESSION['" + filename + "UserDB']) && !empty($_SESSION['" + filename + "DatabaseDB'])) {\n")
    else:
        f.write("if (!empty($_SESSION['" + filename + "PathDB'])) {\n")
    if (dbtype != "sqlite"):
        f.write("    try{\n")
        f.write('    $conn =new PDO("')
        if (dbtype == "MySQL"):
            f.write('mysql:host=".')
        else:
            f.write('pgsql:host=".')
        f.write("$_SESSION['" + filename + "HostDB']")
        f.write('.";dbname=".')
        f.write("$_SESSION['" + filename + "DatabaseDB']")
        f.write(", $_SESSION['" + filename + "UserDB'],")
        f.write(" $_SESSION['" + filename + "PasswordDB']);\n")
        f.write("     $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);\n")
        f.write("     $_SESSION['" + filename + "Connected'] = 1;\n")
        f.write("    } catch (PDOException $e) {\n")
        f.write('     echo"<script>alert(')
        f.write("'Could not connect to the Database'")
        f.write(')</script>";\n')
        f.write("    }\n")
    else:
        f.write("    try{\n")
        f.write('        $conn =new PDO("sqlite:".')
        f.write("        $_SESSION['" + filename + "PathDB']")
        f.write(');\n')
        f.write("        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);\n")
        f.write("        $_SESSION['" + filename + "Connected'] = 1;\n")

        f.write("    } catch (PDOException $e) {\n")
        f.write('        echo"<script>alert(')
        f.write("'Could not connect to the Database'")
        f.write(')</script>";\n')
        f.write("    }\n")

    f.write("}\n")

    f.write("$_SESSION['PageName']='" + filename + "';\n")
    f.write("if (isset($_REQUEST['PageName'])) {\n")
    f.write('    $_SESSION["PageName"] = "' + filename + '";\n')
    f.write("    echo'<meta http-equiv=" + '"refresh"' + 'content="0; URL=Copy.php" />' + "';\n")
    f.write("}\n")
    # if (isset($_REQUEST['PageName'])) {
    # $_SESSION["PageName"] = "MySQL_Project";
    # echo '<meta http-equiv="refresh" content="0; URL=Copy.php" />';
    # }
    f.write("if(empty($_SESSION['" + filename + "Title'])) {\n")
    f.write("$_SESSION['" + filename + "Title'] ='" + filename + "';\n")
    f.write("}\n")
    f.write("if(empty($_SESSION['" + filename + "CurrentPage'])) {\n")
    f.write("$_SESSION['" + filename + "CurrentPage'] = '" + wantedtables[0] + "';\n")
    f.write("}\n")
    for i in range(tableslength):
        f.write("if(isset($_REQUEST['" + wantedtables[i] + "'])) {\n")
        f.write("    $_SESSION['" + filename + "CurrentPage'] = $_REQUEST['" + wantedtables[i] + "'];\n")
        f.write('}\n')
    f.write("?>\n")
    f.close()

def Head(userID, filename):
    f = open(filename + ".php", "a+")
    f.write("    <head>\n")  # done
    f.write("        <?php\n")  # done
    # the line below change the name according to the user
    f.write("        if(!empty($_SESSION['" + filename + "Title'])){\n")

    f.write('            echo"<title>".' + "$_SESSION['" + filename + "Title']" + '."</title>";\n')

    f.write("        } else {\n")
    f.write("            echo'<title>Login</title>';\n")
    f.write("        }\n")
    f.write("        ?>\n")
    f.write("        <meta charset='utf-8'>\n")
    f.write("        <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>\n")
    f.write(
        "        <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>\n")
    f.write(
        "        <script src='https://code.jquery.com/jquery-3.3.1.slim.min.js' integrity='sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo' crossorigin='anonymous'></script>\n")
    # f.write("        <script src='utf-8' integrity='' crossorigin=''>\n")
    f.write(
        "        <script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js' integrity='sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1' crossorigin='anonymous'></script>\n")
    f.write(
        "        <script src='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js' integrity='sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM' crossorigin='anonymous'></script>\n")
    # f.write(
    #     "        <link href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css' rel='stylesheet'/>\n")
    # f.write("        <script type='text/javascript' src='./javascript/myJavascript.js'></script>\n")
    f.write("        <?php\n")
    f.write("        if(!empty($_SESSION['sqlite_ProjectConnected'])){\n")
    f.write("            try{\n")
    f.write('                $conn2 =new PDO("sqlite:'+os.getcwd()+'\Data.sqlite3");\n')
    f.write('                $sql = "SELECT Design FROM History WHERE PageName ='
            + "'" + filename + "'" + ' and user=' + "'" + str(userID) + "'" + '";\n')
    f.write('                $getresult = $conn2->query($sql);\n')
    f.write('                $result = $getresult->fetch();\n')
    f.write('                $sql = "SELECT URL FROM Designs WHERE Sr= '+"'"+'$result[0]'+"'"+'";\n')
    f.write('                $getresult = $conn2->query($sql);\n')
    f.write('                $result = $getresult->fetch();\n')
    f.write('                echo "<link rel=' + "'stylesheet' href='"+ '"' + ".$result[0]."+ '"' + "'>" + '";\n')
    f.write("            }catch(Exception $e){\n")
    f.write("                echo'<script>alert(" + '"could not get Style File"' + ")</script>';\n")
    f.write("            }\n")
    f.write("        }else{\n")
    f.write('                echo "<link rel=' + "'stylesheet' href='https://drive.google.com/uc?id=1VA6zA6oHJXwBgcgnUc4lTOaCrx0TH0Fp'>" + '";\n')
    f.write("        }\n")
    f.write("        ?>\n")

    # $sql = "SELECT Design FROM History WHERE PageName =".$_SESSION["PageName"];
    # $getresult = $conn->query($sql);
    # if ($getresult["Design"] == "MyStyle"){
    # echo "<link rel='stylesheet' href='./Stylesheets/MyStyle.css'>";
    # } else {
    # echo "<link rel='stylesheet' href='./Stylesheets/Default.css'>";
    # }
    # f.write("        <link rel='stylesheet' href='./Stylesheets/MyStyle.css'>\n")
    # f.write("        <link rel='stylesheet' href='./Stylesheets/stylesheet1.css'>\n")
    f.write("    </head>\n")
    f.close()


def NavBar(wantedtables, filename, dbtype="sqlite"):
    tableslength = len(wantedtables)
    f = open(filename + ".php", "a+")
    f.write("        <nav class='navbar navbar-expand-lg navbar-light bg-light'>\n")
    f.write("            <?php\n")  # done
    for i in range(tableslength):
        f.write("            if ($_SESSION['" + filename + "CurrentPage'] == '" + wantedtables[
            i] + "' && !empty($_SESSION['" + filename + "Connected'])) {\n")
        f.write('                echo "' + "<h1 id='logoh1'>" + wantedtables[i] + "</h1>" + '";\n')
        f.write("            }\n")
    f.write("            if(empty($_SESSION['" + filename + "Connected'])){\n")
    f.write('                echo "' + "<h1 id='logoh1'>DB</h1>" + '";\n')
    f.write("            } \n")
    f.write("            ?>\n")
    f.write("            <hr>\n")
    f.write(
        "            <button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarSupportedContent' aria-controls='navbarSupportedContent' aria-expanded='false' aria-label='Toggle navigation'>\n")
    f.write("                <span class='navbar-toggler-icon'></span>\n")
    f.write("            </button>\n")
    f.write("            <div class='collapse navbar-collapse' id='navbarSupportedContent'>\n")
    f.write("                <ul class='navbar-nav mr-auto'>\n")
    f.write("                    <?php\n")
    if (dbtype != "sqlite"):
        f.write(
            "                    if (!empty($_SESSION['" + filename + "HostDB']) && !empty($_SESSION['" + filename + "UserDB']) && !empty($_SESSION['" + filename + "DatabaseDB'])) {\n")

        f.write('                        echo"<li class=' + " 'nav-item'>" + '";\n')

        f.write('                        echo"<h1 id=' + " 'logoh1'>Connected successfully</h1>" + '";\n')

        f.write('                        echo"</li>";\n')

        f.write('                        echo"<form>";\n')
        f.write('                        echo"<li class=' + " 'nav-item'>" + '";\n')
        f.write('                        echo"<button class=' + "'btn btn-outline-success my-2 my-sm-3'" + " name='"
                + "PageName'" + " value='" + "MySQL_Project" + "' type='" + "submit'" + '>Look and feel</button>";\n')
        f.write('                        echo"</li>";\n')
        f.write('                        echo"</form>";\n')
        # <form>
        # <button class='btn btn-outline-success my-2 my-sm-0' name='PageName' value='MySQL_Project' type='submit'>Look and feel</button>
        # </form>

        f.write("                    } else {\n")

        f.write('                        echo"<form class=')
        f.write(" 'form-inline my-2 my-lg-0' method=" + " 'post'>" + '";\n')

        f.write('                        echo"<li class=' + " 'nav-item'>" + '";\n')

        f.write('                        echo"<input class=')
        f.write(" 'form-control mr-sm-2' name='Host' type='text' placeholder='Host'>" + '";\n')
        f.write('                        echo"</li>";\n')

        f.write('                        echo"<li class=' + " 'nav-item'>" + '";\n')

        f.write('                        echo"<input class=')
        f.write(" 'form-control mr-sm-2' name='User' type='text' placeholder='User'>" + '";\n')
        f.write('                        echo"</li>";\n')

        f.write('                        echo"<li class=' + " 'nav-item'>" + '";\n')

        f.write('                        echo"<input class=')
        f.write(" 'form-control mr-sm-2' name='Password' type='text' placeholder='Password'>" + ' ";\n')
        f.write('                        echo"</li>";\n')

        f.write('                        echo"<li class=' + "'nav-item'>" + '";\n')

        f.write('                        echo"<input class=')
        f.write(" 'form-control mr-sm-2' name='Database' type='text' placeholder='Database'>" + '";\n')
        f.write('                        echo"</li>";\n')

        f.write('                        echo"<li class=' + "'nav-item'>" + '";\n')

        f.write('                        echo"<button class=')
        f.write("'btn btn-outline-success my-2 my-sm-0' name='Connect' type='search'>Connect</button>" + '";\n')

        f.write('                        echo"</li>";\n')

        f.write('                        echo"</form>";\n')
        f.write("                    }\n")
    else:
        f.write("                    if (!empty($_SESSION['" + filename + "PathDB'])) {\n")

        f.write('                        echo"<li class=');
        f.write(" 'nav-item'>");
        f.write('";\n');

        f.write('                        echo"<h1 id=');
        f.write(" 'logoh1'>Connected successfully</h1>");
        f.write('";\n');
        f.write('                        echo"</li>";\n')

        f.write('                        echo"<form>";\n')
        f.write('                        echo"<li class=' + " 'nav-item'>" + '";\n')
        f.write('                        echo"<button class=' + "'btn btn-outline-success my-2 my-sm-3'" + " name='"
                + "PageName'" + " value='" + "MySQL_Project" + "' type='" + "submit'" + '>Look and feel</button>";\n')
        f.write('                        echo"</li>";\n')
        f.write('                        echo"</form>";\n')

        f.write("                    } else {\n")

        f.write('                        echo"<form class=')
        f.write("'form-inline my-2 my-lg-0' method=")
        f.write("'post'>")
        f.write('";\n')

        f.write('                        echo"<li class=')
        f.write("'nav-item'>")
        f.write('";\n')

        f.write('                        echo"<input class=')
        f.write("'form-control mr-sm-2' name='Path' type='text' placeholder='Path with the filename and extension'>")
        f.write('";\n')
        f.write('                        echo"</li>";\n')

        f.write('                        echo"<button class=')
        f.write("'btn btn-outline-success my-2 my-sm-0' name='Connect' type='search'>Connect</button>")
        f.write('";\n')
        f.write('                        echo"</li>";\n')

        f.write('                        echo"</form>";\n')
        f.write("                    }\n")

    f.write("                    if (isset($_REQUEST['Connect'])) {\n")
    if (dbtype != "sqlite"):
        f.write(
            "                        $input = !empty($_POST['Host']) && !empty($_POST['User']) && !empty($_POST['Database']);\n")
    else:
        f.write("                        $input = !empty($_POST['Path']);\n")

    f.write("                        if ($input) {\n")
    if (dbtype != "sqlite"):
        f.write("                            if (empty($_POST['Password'])) {\n")
        f.write("                                try{\n")
        f.write('                                    $conn =new PDO("')
        if (dbtype == "MySQL"):
            f.write('mysql:host=".')
        else:
            f.write('pgsql:host=".')
        f.write("$_POST['Host']")
        f.write('.";dbname=".')
        f.write("$_POST['Database']")
        f.write(", $_POST['User'],")
        f.write(' "");\n')
        f.write("                                    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);\n")
        f.write("                                    $_SESSION['" + filename + "HostDB'] = $_POST['Host'];\n")
        f.write("                                    $_SESSION['" + filename + "UserDB'] = $_POST['User'];\n")
        f.write("                                    $_SESSION['" + filename + "PasswordDB'] = '';\n")
        f.write("                                    $_SESSION['" + filename + "DatabaseDB'] = $_POST['Database'];\n")
        f.write("                                    $_SESSION['" + filename + "Connected'] = 1;\n")
        f.write("                                    echo" + '"' + "<meta http-equiv='refresh' content='0; URL="
                + filename + ".php' />" + '"' + ";\n")
        f.write("                                } catch (PDOException $e) {\n")
        f.write('                                    echo"<script>alert(')
        f.write("'Could not connect to the Database'")
        f.write(')</script>";\n')
        f.write("                                }\n")
        f.write("                            } else {\n")
        f.write("                                try{\n")
        f.write('                                    $conn =new PDO("')
        if (dbtype == "MySQL"):
            f.write('mysql:host=".')
        else:
            f.write('pgsql:host=".')
        f.write("$_POST['Host']")
        f.write('.";dbname=".')
        f.write("$_POST['Database']")
        f.write(", $_POST['User'],")
        f.write(" $_POST['Password']);\n")
        f.write("                                    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);\n")
        f.write("                                    $_SESSION['" + filename + "HostDB'] = $_POST['Host'];\n")
        f.write("                                    $_SESSION['" + filename + "UserDB'] = $_POST['User'];\n")
        f.write("                                    $_SESSION['" + filename + "PasswordDB'] = $_POST['Password'];\n")
        f.write("                                    $_SESSION['" + filename + "DatabaseDB'] = $_POST['Database'];\n")
        f.write("                                    $_SESSION['" + filename + "Connected'] = 1;\n")
        f.write("                                    echo" + '"' + "<meta http-equiv='refresh' content='0; URL="
                + filename + ".php' />" + '"' + ";\n")
        f.write("                                } catch (PDOException $e) {\n")
        f.write('                                    echo"<script>alert(')
        f.write("'Could not connect to the Database'")
        f.write(')</script>";\n')
        f.write("                                }\n")
        f.write("                            }\n")
    else:
        f.write("                                try{\n")
        f.write('                                    $conn =new PDO("sqlite:".')
        f.write("$_POST['Path']")
        f.write(');\n')
        f.write("                                    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);\n")
        f.write("                                    $_SESSION['" + filename + "PathDB'] = $_POST['Path'];\n")
        f.write("                                    $_SESSION['" + filename + "Connected'] = 1;\n")
        f.write("                                    echo" + '"' + "<meta http-equiv='refresh' content='0; URL="
                + filename + ".php' />" + '"' + ";\n")
        f.write("                                } catch (PDOException $e) {\n")
        f.write('                                    echo"<script>alert(')
        f.write("'Could not connect to the Database'")
        f.write(')</script>";\n')
        f.write("                                }\n")

    f.write("                        } else {\n")
    f.write('                            echo"<script>alert(')
    f.write("'Could not connect to the Database'")
    f.write(')</script>";\n')
    f.write("                        }\n")
    f.write("                    }\n")
    f.write("                    ?>\n")
    f.write("                </ul>\n")
    f.write("            </div>\n")
    f.write("        </nav>\n")

    f.close()


def NavBarButtons(wantedtables, filename, dbtype="sqlite"):
    tableslength = len(wantedtables)
    f = open(filename + ".php", "a+")
    f.write("        <div class='container-fluid margin-top-1'>\n")
    f.write("            <?php\n")
    if (dbtype != "sqlite"):
        f.write(
            "            if (!empty($_SESSION['" + filename + "HostDB']) && !empty($_SESSION['" + filename + "UserDB']) && !empty($_SESSION['" + filename + "DatabaseDB'])) {\n")
    else:
        f.write("            if (!empty($_SESSION['" + filename + "PathDB'])) {\n")

    f.write('                echo "<form class=')
    f.write("'form-inline my-2 my-lg-0'")
    f.write('>";\n')
    for i in range(tableslength):
        f.write('                echo "<button name=')
        f.write("'" + wantedtables[i] + "' value = " + wantedtables[i] + " class='btn generate1'>" + wantedtables[
            i] + "</button>")
        f.write('";\n')

    f.write('                echo "</form>";\n')
    f.write("            } else {\n")
    f.write('                echo "<h1 id=')
    f.write("'logoh1'>Please Connect to the Database to show the list of tables")
    f.write('</h1>";\n')
    f.write("            }\n")

    # for i in range(tableslength):
    #     f.write("            if (isset($_REQUEST['"+wantedtables[i]+"'])) {\n")
    #     f.write("            $_SESSION['CurrentTable'] = '"+wantedtables[i]+"';\n")
    #     f.write("            }\n")

    f.write("            ?>\n")
    f.write("        </div>\n")
    f.close()


def SearchAndTable(wantedtables, wantedcolumns, filename, dbtype="sqlite"):
    tableslength = len(wantedtables)
    columnslength = len(wantedcolumns)
    f = open(filename + ".php", "a+")
    f.write("        <div class='container-fluid mar'>\n")
    f.write('            <table id="allActivities">\n')
    f.write("                <?php\n")
    f.write("                if (!empty($conn)) {\n")
    f.write('                    echo "<div class=' + "'form-inline'>" + '";\n')
    f.write('                    echo "<form class=')
    f.write("'form-inline' action='' method='GET' id='mysearch'" + '>";\n')
    f.write('                    echo "<input class=')
    f.write(
        "'form-control col-md-8' name='searchinput' type='search' placeholder='Search Activities' style='margin-left: 13%;'")
    f.write('>";\n')
    f.write('                    echo "<button class=')
    f.write("'btn btn-outline-success my-2 my-sm-0' type='submit' name='Search'>Search</button>")
    f.write('";\n')
    f.write('                    echo "<select name=')
    f.write("reference")
    f.write('>";\n')
    for i in range(tableslength):
        f.write("            if ($_SESSION['" + filename + "CurrentPage'] == '" + wantedtables[i] + "') {\n")
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                echo "<option value=')
                if (wantedcolumns[j][2] == 1):
                    f.write("'" + wantedcolumns[j][1] + "' selected>" + wantedcolumns[j][1] + "</option>")
                else:
                    f.write("'" + wantedcolumns[j][1] + "'>" + wantedcolumns[j][1] + "</option>")
                f.write('";\n')
        f.write("            }\n")

    f.write('                    echo "</select>";\n')
    f.write('                    echo "</form>";\n')
    f.write('                    echo "</div>";\n')

    f.write("        if (isset($_REQUEST['Search'])) {\n")
    f.write("            $input = $_GET['searchinput'];\n")
    f.write("            if (empty($input)) {\n")

    for i in range(tableslength):
        f.write("            if ($_SESSION['" + filename + "CurrentPage'] == '" + wantedtables[i] + "') {\n")
        f.write('                echo"<tr>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                echo"<th id=')
                f.write("'" + wantedcolumns[j][1] + "'>" + wantedcolumns[j][1] + "</th>" + '";\n')
        f.write('                echo"<th id=' + "actions'>Actions</th>" + '";\n')
        f.write('                echo"</tr>";\n')

        f.write('                echo"<form>";\n')
        f.write('                echo"<tr>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                echo"<td id=')
                f.write("'" + wantedcolumns[j][1] + "'><input type='text' name='" + wantedcolumns[j][1] + "'></td>")
                f.write('";\n')
        f.write('                echo "<td>')
        f.write("<button name='add' type='submit' class='btn AcceptBtn'>Add</button>" + "</td>" + '";\n')
        f.write('                echo"</tr>";\n')
        f.write('                echo"</form>";\n')
        argu = ""
        arguinput = ""
        if (dbtype == "PostgreSQL"):
            for j in range(columnslength):
                if (wantedcolumns[j][0] == i):
                    argu = argu + wantedcolumns[j][1] + '","'
                    arguinput = arguinput + ".$_GET['" + wantedcolumns[j][1] + "']."
                    arguinput = arguinput + "'" + '","' + "'"
            argu = argu[:-2]
        else:
            for j in range(columnslength):
                if (wantedcolumns[j][0] == i):
                    argu = argu + wantedcolumns[j][1] + ","
                    arguinput = arguinput + '.$_GET["' + wantedcolumns[j][1] + '"].'
                    arguinput = arguinput + '"' + "','" + '"'
            argu = argu[:-1]
        arguinput = arguinput[:-3]
        f.write("                if (isset($_REQUEST['add'])) {\n")
        f.write('                     try{\n')
        if (dbtype == "PostgreSQL"):
            f.write('                     $sqlgetStatus =' + " 'INSERT INTO " + '"' + wantedtables[i] + '"' + ' ("' +
                    argu + ') VALUES("' + "'" + arguinput + ");';\n")
        else:
            f.write('                     $sqlgetStatus = "INSERT INTO ' + wantedtables[i] + ' (' + argu + ') VALUES(')
            f.write("'")
            f.write('"')
            f.write(" " + arguinput)
            f.write(');";\n')
        f.write("                     $getStatus = $conn->exec($sqlgetStatus);\n")
        f.write("                     $conn = null;\n")
        f.write("                     echo '<meta http-equiv=")
        f.write('"refresh" content="0; URL=' + filename + '.php"')
        f.write("/>';\n")
        f.write('                     }catch(Exception $e){\n')
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                         echo'<script type=" + '"text/javascript">confirm("' + "'.$e->getMessage().'")
        f.write('");</script>' + "';\n")
        f.write('                     }\n')
        f.write("                }\n")
        if (dbtype == "PostgreSQL"):
            f.write("                $sqlUsers = 'SELECT " + '"' + argu + ' FROM "' + wantedtables[i] + '"' + ";';\n")
        else:
            f.write('                $sqlUsers = "SELECT ' + argu + ' FROM ' + wantedtables[i] + ';";\n')
        f.write('                $result = $conn->query($sqlUsers);\n')
        f.write('                if (!empty($result)) {\n')
        f.write('                    foreach ($result as $row) {\n')
        f.write('                        echo "<tr>";\n')
        f.write('                        echo "<form>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                        echo "<td><input type=')
                f.write("'text' name='" + wantedcolumns[j][1] + "' value='")
                f.write('".$row["' + wantedcolumns[j][1] + '"] ."')
                f.write("'>")
                f.write('</td>";\n')

        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write("                        $UserSr = $row['" + wantedcolumns[j][1] + "'];\n")

        f.write('                        echo "<td><button name=')
        f.write("'delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>")
        f.write('";\n')

        f.write('                        echo "<button name=')
        f.write("'savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button>")
        f.write('</td>";\n')
        f.write('                        echo "</form>";\n')

        f.write("                        if (isset($_REQUEST['delete'])) {\n")
        f.write("                            try{\n")
        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write('                            $sqlgetStatus = "DELETE FROM ' + wantedtables[i] + ' WHERE ' +
                        wantedcolumns[j][1] + ' =')
        f.write("'" + '"' + ". $_GET['delete'] ." + '"' + "';" + '";\n')
        f.write('                            $conn->exec($sqlgetStatus);\n')
        f.write('                            $conn = null;\n')
        f.write("                            echo '<meta http-equiv=")
        f.write('"refresh" content="0; URL=' + filename + '.php"')
        f.write("/>';\n")
        f.write('                             }catch(Exception $e){\n')
        # $_REQUEST['delete']=null;
        f.write("                                 $_REQUEST['delete']=null;\n")
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                             }\n')
        f.write("                        } else if(isset($_REQUEST['savechanges'])){\n")
        f.write("                            try{\n")
        f.write("                            $PassedSr = $_GET['savechanges'];\n")
        f.write('                            $sqlgetStatus = "UPDATE ' + wantedtables[i])
        sargu = ""
        for n in range(columnslength):
            if (wantedcolumns[n][0] == i):
                sargu = sargu + wantedcolumns[n][1] + "='" + '"' + ". $_GET['" + wantedcolumns[n][
                    1] + "'] ." + '"' + "',"
        sargu = sargu[:-1]
        f.write(" SET " + sargu)
        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write(" WHERE " + wantedcolumns[j][1] + " ='$PassedSr';")
        f.write('";\n')
        f.write('                            $conn->exec($sqlgetStatus);\n')
        f.write('                            $conn = null;\n')
        f.write("                            echo '<meta http-equiv=")
        f.write('"refresh" content="0; URL=' + filename + '.php"' + "/>';\n");
        f.write('                             }catch(Exception $e){\n')
        f.write("                                 $_REQUEST['savechanges']=null;\n")
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                             }\n')
        f.write("                        }\n")

        f.write('                        echo "</tr>";\n')
        f.write('                    }\n')
        f.write('                }\n')

        f.write("            }\n")
    f.write("            } else {\n")
    f.write("                if (empty(preg_replace('/\s+/', '', $input))) {\n")
    for i in range(tableslength):
        f.write("            if ($_SESSION['" + filename + "CurrentPage'] == '" + wantedtables[i] + "') {\n")
        f.write('                echo"<tr>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                echo"<th id=')
                f.write("'" + wantedcolumns[j][1] + "'>" + wantedcolumns[j][1] + "</th>" + '";\n')
        f.write('                echo"<th id=' + "actions'>Actions</th>" + '";\n')
        f.write('                echo"</tr>";\n')

        f.write('                echo"<form>";\n')
        f.write('                echo"<tr>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                echo"<td id=')
                f.write("'" + wantedcolumns[j][1] + "'><input type='text' name='" + wantedcolumns[j][1] + "'></td>")
                f.write('";\n')
        f.write('                echo "<td>')
        f.write("<button name='add' type='submit' class='btn AcceptBtn'>Add</button></td>" + '";\n')
        f.write('                echo"</tr>";\n')
        f.write('                echo"</form>";\n')
        argu = ""
        arguinput = ""
        if (dbtype == "PostgreSQL"):
            for j in range(columnslength):
                if (wantedcolumns[j][0] == i):
                    argu = argu + wantedcolumns[j][1] + '","'
                    arguinput = arguinput + ".$_GET['" + wantedcolumns[j][1] + "']."
                    arguinput = arguinput + "'" + '","' + "'"
            argu = argu[:-2]
        else:
            for j in range(columnslength):
                if (wantedcolumns[j][0] == i):
                    argu = argu + wantedcolumns[j][1] + ","
                    arguinput = arguinput + '.$_GET["' + wantedcolumns[j][1] + '"].'
                    arguinput = arguinput + '"' + "','" + '"'
            argu = argu[:-1]
        arguinput = arguinput[:-3]
        f.write("                if (isset($_REQUEST['add'])) {\n")
        f.write('                     try{\n')
        if (dbtype == "PostgreSQL"):
            f.write('                     $sqlgetStatus =' + " 'INSERT INTO " + '"' + wantedtables[i] + '"' + ' ("' +
                    argu + ') VALUES("' + "'" + arguinput + ");';\n")
        else:
            f.write('                     $sqlgetStatus = "INSERT INTO ' + wantedtables[i] + ' (' + argu + ') VALUES(')
            f.write("'")
            f.write('"')
            f.write(" " + arguinput)
            f.write(');";\n')
        f.write("                     $getStatus = $conn->exec($sqlgetStatus);\n")
        f.write("                     $conn = null;\n")
        f.write(
            "                     echo '<meta http-equiv=" + '"refresh" content="0; URL=' + filename + '.php"' + "/>';\n")
        f.write('                     }catch(Exception $e){\n')
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                     }\n')
        f.write("                }\n")
        if (dbtype == "PostgreSQL"):
            f.write("                $sqlUsers = 'SELECT " + '"' + argu + ' FROM "' + wantedtables[i] + '"' + ";';\n")
        else:
            f.write('                $sqlUsers = "SELECT ' + argu + ' FROM ' + wantedtables[i] + ';";\n')
        f.write('                $result = $conn->query($sqlUsers);\n')
        f.write('                if (!empty($result)) {\n')
        f.write('                    foreach ($result as $row) {\n')
        f.write('                        echo "<tr>";\n')
        f.write('                        echo "<form>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                        echo "<td><input type=')
                f.write("'text' name='" + wantedcolumns[j][1] + "' value='")
                f.write('".$row["' + wantedcolumns[j][1] + '"] ."' + "'>" + '</td>";\n')

        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write("                        $UserSr = $row['" + wantedcolumns[j][1] + "'];\n")

        f.write('                        echo "<td><button name=')
        f.write("'delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>" + '";\n')

        f.write('                        echo "<button name=')
        f.write("'savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button>" + '</td>";\n')
        f.write('                        echo "</form>";\n')

        f.write("                        if (isset($_REQUEST['delete'])) {\n")
        f.write("                            try{\n")
        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write('                            $sqlgetStatus = "DELETE FROM ' + wantedtables[i] + ' WHERE ' +
                        wantedcolumns[j][1] + ' =')
        f.write("'" + '"' + ". $_GET['delete'] ." + '"' + "';" + '";\n')
        f.write('                            $conn->exec($sqlgetStatus);\n')
        f.write('                            $conn = null;\n')
        f.write(
            "                            echo '<meta http-equiv=" + '"refresh" content="0; URL=' + filename + '.php"' + "/>';\n")
        f.write('                            }catch(Exception $e){\n')
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 $_REQUEST['delete']=null;\n")
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                            }\n')
        f.write("                        } else if(isset($_REQUEST['savechanges'])){\n")
        f.write("                            try{\n")
        f.write("                            $PassedSr = $_GET['savechanges'];\n")
        f.write('                            $sqlgetStatus = "UPDATE ' + wantedtables[i])
        sargu = ""
        for n in range(columnslength):
            if (wantedcolumns[n][0] == i):
                sargu = sargu + wantedcolumns[n][1]
                sargu = sargu + "='"
                sargu = sargu + '"'
                sargu = sargu + ". $_GET['" + wantedcolumns[n][1] + "'] ."
                sargu = sargu + '"'
                sargu = sargu + "',"
        sargu = sargu[:-1]
        f.write(" SET " + sargu)
        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write(" WHERE " + wantedcolumns[j][1] + " ='$PassedSr';")
        f.write('";\n')
        f.write('                            $conn->exec($sqlgetStatus);\n')
        f.write('                            $conn = null;\n')
        f.write("                            echo '<meta http-equiv=");
        f.write('"refresh" content="0; URL=' + filename + '.php"');
        f.write("/>';\n")
        f.write('                            }catch(Exception $e){\n')
        f.write("                                 $_REQUEST['savechanges']=null;\n")
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                            }\n')
        f.write("                        }\n")

        f.write('                        echo "</tr>";\n')
        f.write('                    }\n')
        f.write('                }\n')

        f.write("            }\n")

    f.write("                }else {\n")

    for i in range(tableslength):
        f.write("            if ($_SESSION['" + filename + "CurrentPage'] == '" + wantedtables[i] + "') {\n")
        f.write('                echo"<tr>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                echo"<th id=')
                f.write("'" + wantedcolumns[j][1] + "'>" + wantedcolumns[j][1] + "</th>" + '";\n')
        f.write('                echo"<th id=' + "actions'>Actions</th>" + '";\n')
        f.write('                echo"</tr>";\n')

        f.write('                echo"<form>";\n')
        f.write('                echo"<tr>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                echo"<td id=')
                f.write("'" + wantedcolumns[j][1] + "'><input type='text' name='" + wantedcolumns[j][
                    1] + "'></td>" + '";\n')
        f.write('                echo "<td>')
        f.write("<button name='add' type='submit' class='btn AcceptBtn'>Add</button>" + '</td>";\n')
        f.write('                echo"</tr>";\n')
        f.write('                echo"</form>";\n')
        argu = ""
        arguinput = ""
        if (dbtype == "PostgreSQL"):
            for j in range(columnslength):
                if (wantedcolumns[j][0] == i):
                    argu = argu + wantedcolumns[j][1] + '","'
                    arguinput = arguinput + ".$_GET['" + wantedcolumns[j][1] + "']."
                    arguinput = arguinput + "'" + '","' + "'"
            argu = argu[:-2]
        else:
            for j in range(columnslength):
                if (wantedcolumns[j][0] == i):
                    argu = argu + wantedcolumns[j][1] + ","
                    arguinput = arguinput + '.$_GET["' + wantedcolumns[j][1] + '"].'
                    arguinput = arguinput + '"' + "','" + '"'
            argu = argu[:-1]
        arguinput = arguinput[:-3]
        f.write("                if (isset($_REQUEST['add'])) {\n")
        f.write('                     try{\n')
        if (dbtype == "PostgreSQL"):
            f.write('                     $sqlgetStatus =' + " 'INSERT INTO " + '"' + wantedtables[i] + '"' + ' ("' +
                    argu + ') VALUES("' + "'" + arguinput + ");';\n")
        else:
            f.write('                     $sqlgetStatus = "INSERT INTO ' + wantedtables[i] + ' (' + argu + ') VALUES(')
            f.write("'")
            f.write('"')
            f.write(" " + arguinput)
            f.write(');";\n')
        f.write("                     $getStatus = $conn->exec($sqlgetStatus);\n")
        f.write("                     $conn = null;\n")
        f.write("                     echo '<meta http-equiv=")
        f.write(' "refresh" content="0; URL=' + filename + '.php"')
        f.write(" />';\n")
        f.write('                     }catch(Exception $e){\n')
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                     }\n')
        f.write("                }\n")
        if (dbtype == "PostgreSQL"):
            f.write("                $sqlUsers = 'SELECT " + '"' + argu + ' FROM "' + wantedtables[
                i] + '"' + ' WHERE "' + "'" + ' . $_GET["reference"] .' + "'" + '" =')
            f.write('"')
            f.write("'. $_GET['searchinput'] .'")
            f.write('"')
            f.write("';\n")
        else:
            f.write('                $sqlUsers = "SELECT ' + argu + ' FROM ' + wantedtables[
                i] + ' WHERE " . $_GET["reference"] ." =')
            f.write("'")
            f.write('". $_GET["searchinput"] ."')
            f.write("'")
            f.write('";\n')
        f.write('                $result = $conn->query($sqlUsers);\n')
        f.write('                if (!empty($result)) {\n')
        f.write('                    foreach ($result as $row) {\n')
        f.write('                        echo "<tr>";\n')
        f.write('                        echo "<form>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                        echo "<td><input type=')
                f.write("'text' name='" + wantedcolumns[j][1] + "' value='")
                f.write('".$row["' + wantedcolumns[j][1] + '"] ."' + "'>" + '</td>";\n')

        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write("                        $UserSr = $row['" + wantedcolumns[j][1] + "'];\n")

        f.write('                        echo "<td><button name=')
        f.write("'delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>" + '";\n')

        f.write('                        echo "<button name=')
        f.write("'savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button>" + '</td>";\n')
        f.write('                        echo "</form>";\n')

        f.write("                        if (isset($_REQUEST['delete'])) {\n")
        f.write("                            try{\n")
        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write('                            $sqlgetStatus = "DELETE FROM ' + wantedtables[i] + ' WHERE ' +
                        wantedcolumns[j][1] + ' =')
        f.write(" '" + ' "' + " . $_GET['delete'] ." + ' "' + " ';" + ' ";\n')
        f.write('                            $conn->exec($sqlgetStatus);\n')
        f.write('                            $conn = null;\n')
        f.write("                            echo '<meta http-equiv=")
        f.write('"refresh" content="0; URL=' + filename + '.php"' + "/>';\n")
        f.write('                            }catch(Exception $e){\n')
        f.write("                                 $_REQUEST['delete']=null;\n")
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                            }\n')
        f.write("                        } else if(isset($_REQUEST['savechanges'])){\n")
        f.write("                            try{\n")
        f.write("                            $PassedSr = $_GET['savechanges'];\n")
        f.write('                            $sqlgetStatus = "UPDATE ' + wantedtables[i])
        sargu = ""
        for n in range(columnslength):
            if (wantedcolumns[n][0] == i):
                sargu = sargu + wantedcolumns[n][1]
                sargu = sargu + "='"
                sargu = sargu + '"'
                sargu = sargu + ". $_GET['" + wantedcolumns[n][1] + "'] ."
                sargu = sargu + '"'
                sargu = sargu + "',"
        sargu = sargu[:-1]
        f.write(" SET " + sargu)
        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write(" WHERE " + wantedcolumns[j][1] + " ='$PassedSr';")
        f.write('";\n')
        f.write('                            $conn->exec($sqlgetStatus);\n')
        f.write('                            $conn = null;\n')
        f.write("                            echo '<meta http-equiv=")
        f.write(' "refresh" content="0; URL=' + filename + '.php"');
        f.write(" />';\n");
        f.write('                            }catch(Exception $e){\n')
        f.write("                                 $_REQUEST['savechanges']=null;\n")
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                            }\n')
        f.write("                        }\n")

        f.write('                        echo "</tr>";\n')
        f.write('                    }\n')
        f.write('                }\n')

        f.write("            }\n")

    f.write("                }\n")
    f.write("            }\n")
    f.write("        } else {\n")

    for i in range(tableslength):
        f.write("            if ($_SESSION['" + filename + "CurrentPage'] == '" + wantedtables[i] + "') {\n")
        f.write('                echo"<tr>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                echo"<th id=');
                f.write(" '" + wantedcolumns[j][1] + "'>" + wantedcolumns[j][1] + "</th>");
                f.write('";\n');
        f.write('                echo"<th id=');
        f.write("actions'>Actions</th>");
        f.write('";\n');
        f.write('                echo"</tr>";\n')

        f.write('                echo"<tr>";\n')
        f.write('                echo"<form>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                echo"<td id=')
                f.write("'" + wantedcolumns[j][1] + "'><input type='text' name='" + wantedcolumns[j][
                    1] + "'></td>" + '";\n')
        f.write('                echo "<td>')
        f.write("<button name='add' type='submit' class='btn AcceptBtn'>Add</button></td>" + '";\n')
        f.write('                echo"</form>";\n')
        f.write('                echo"</tr>";\n')

        argu = ""
        arguinput = ""
        if (dbtype == "PostgreSQL"):
            for j in range(columnslength):
                if (wantedcolumns[j][0] == i):
                    argu = argu + wantedcolumns[j][1] + '","'
                    arguinput = arguinput + ".$_GET['" + wantedcolumns[j][1] + "']."
                    arguinput = arguinput + "'" + '","' + "'"
            argu = argu[:-2]
        else:
            for j in range(columnslength):
                if (wantedcolumns[j][0] == i):
                    argu = argu + wantedcolumns[j][1] + ","
                    arguinput = arguinput + '.$_GET["' + wantedcolumns[j][1] + '"].'
                    arguinput = arguinput + '"' + "','" + '"'
            argu = argu[:-1]
        arguinput = arguinput[:-3]
        f.write("                if (isset($_REQUEST['add'])) {\n")
        f.write('                     try{\n')
        if (dbtype == "PostgreSQL"):
            f.write('                     $sqlgetStatus =' + " 'INSERT INTO " + '"' + wantedtables[i] + '"' + ' ("' +
                    argu + ') VALUES("' + "'" + arguinput + ");';\n")
        else:
            f.write('                     $sqlgetStatus = "INSERT INTO ' + wantedtables[i] + ' (' + argu + ') VALUES(')
            f.write("'")
            f.write('"')
            f.write(" " + arguinput)
            f.write(');";\n')
        f.write("                     $getStatus = $conn->exec($sqlgetStatus);\n")
        f.write("                     $conn = null;\n")
        f.write("                     echo '<meta http-equiv=")
        f.write(' "refresh" content="0; URL=' + filename + '.php"');
        f.write("/>';\n");
        f.write('                     }catch(Exception $e){\n')
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                     }\n')
        f.write("                }\n")
        if (dbtype == "PostgreSQL"):
            f.write("                $sqlUsers = 'SELECT " + '"' + argu + ' FROM "' + wantedtables[i] + '"' + ";';\n")
        else:
            f.write('                $sqlUsers = "SELECT ' + argu + ' FROM ' + wantedtables[i] + ';";\n')
        f.write('                $result = $conn->query($sqlUsers);\n')
        f.write('                if (!empty($result)) {\n')
        f.write('                    foreach ($result as $row) {\n')
        f.write('                        echo "<tr>";\n')
        f.write('                        echo "<form>";\n')
        for j in range(columnslength):
            if (wantedcolumns[j][0] == i):
                f.write('                        echo "<td><input type=')
                f.write("'text' name='" + wantedcolumns[j][1] + "' value='" + '".$row["' + wantedcolumns[j][
                    1] + '"] ."' + "'>" + '</td>";\n')

        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write("                        $UserSr = $row['" + wantedcolumns[j][1] + "'];\n")

        f.write('                        echo "<td><button name=')
        f.write("'delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>" + '";\n')

        f.write('                        echo "<button name=')
        f.write("'savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button>" + '</td>";\n')
        f.write('                        echo "</form>";\n')

        f.write("                        if (isset($_REQUEST['delete'])) {\n")
        f.write('                            try{\n')
        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write('                            $sqlgetStatus = "DELETE FROM ' + wantedtables[i] + ' WHERE ' +
                        wantedcolumns[j][1] + ' =')
        f.write(" '");
        f.write(' "');
        f.write(". $_GET['delete'] .");
        f.write(' "');
        f.write(" ';");
        f.write('";\n');
        f.write('                            $conn->exec($sqlgetStatus);\n')
        f.write('                            $conn = null;\n')
        f.write("                            echo '<meta http-equiv=");
        f.write(' "refresh" content="0; URL=' + filename + '.php"' + "/>';\n");
        f.write('                            }catch(Exception $e){\n')
        f.write("                                 $_REQUEST['delete']=null;\n")
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                            }\n')
        f.write("                        } else if(isset($_REQUEST['savechanges'])){\n")
        f.write("                            try{\n")
        f.write("                            $PassedSr = $_GET['savechanges'];\n")
        f.write('                            $sqlgetStatus = "UPDATE ' + wantedtables[i])
        sargu = ""
        for n in range(columnslength):
            if (wantedcolumns[n][0] == i):
                sargu = sargu + wantedcolumns[n][1]
                sargu = sargu + "='"
                sargu = sargu + '"'
                sargu = sargu + ". $_GET['" + wantedcolumns[n][1] + "'] ."
                sargu = sargu + '"'
                sargu = sargu + "',"
        sargu = sargu[:-1]
        f.write(" SET " + sargu)
        for j in range(columnslength):
            if (wantedcolumns[j][2] == 1 and wantedcolumns[j][0] == i):
                f.write(" WHERE " + wantedcolumns[j][1] + " ='$PassedSr';")
        f.write('";\n')
        f.write('                            $conn->exec($sqlgetStatus);\n')
        f.write('                            $conn = null;\n')
        f.write(
            "                            echo '<meta http-equiv=" + '"refresh" content="0; URL=' + filename + '.php"' + "/>';\n")
        f.write('                            }catch(Exception $e){\n')
        f.write("                                 $_REQUEST['savechanges']=null;\n")
        # echo '<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
        f.write("                                 echo'<script type=" + '"text/javascript">confirm("'
                + "'.$e->getMessage().'" + '");</script>' + "';\n")
        f.write('                            }\n')
        f.write("                        }\n")

        f.write('                        echo "</tr>";\n')
        f.write('                    }\n')
        f.write('                }\n')

        f.write("            }\n")

    f.write("        }\n")

    f.write("                }\n")
    f.write("                ?>\n")
    f.write('            </table>\n')
    f.write("        </div>\n")
    f.close()


def Footer(filename):
    f = open(filename + ".php", "a+")
    f.write("        <footer>\n")
    f.write("            <div class='row'>\n")
    f.write("                <div class='col-sm-2'>\n")
    f.write("                    <img src='./images/KFUPMLogo.png' alt='Logo' width='250' height='250'>\n")
    f.write("                </div>\n")
    f.write("                <div class = 'col-sm-2' id = 'copyrights'>\n")
    f.write("                    <p>&copy; Murtada Alawami<br>Mohammed Al-Sayed</p>\n")
    f.write("                </div>\n")
    f.write("            </div>\n")
    f.write("        </footer>\n")
    f.close()


def generate(userID,wantedtables, wantedcolumns, filename, dbtype="sqlite"):
    f = open(filename+".php", "w+")
    f.close()
    beforeHTML(userID,wantedtables, filename, dbtype)
    f = open(filename + ".php", "a+")
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.close()
    Head(userID, filename)
    f = open(filename + ".php", "a+")
    f.write("    <body>\n")
    f.close()
    NavBar(wantedtables, filename, dbtype)
    NavBarButtons(wantedtables, filename, dbtype)
    SearchAndTable(wantedtables, wantedcolumns, filename, dbtype)
    Footer(filename)
    f = open(filename + ".php", "a+")
    f.write("    </body>\n")
    f.write("</html>")
    f.close()
    try:
        if (sqlite3.connect("Data.sqlite3")):
                conn = sqlite3.connect("Data.sqlite3")
                cur = conn.cursor()
                cur.execute('INSERT INTO HISTORY (user,PageName,Design) VALUES('+str(userID)+','+"'"+'sqlite_Project'+"'"+',1);')
                conn.commit()
                conn.close()
        else:
                print("Failed")
    except (Exception) as error:
        print(error)

#MySQL
# ta = MySQLTables("project")
# cols = MySQLColumns(ta,"project")
# print(cols)
# generate(1,ta,cols,"MySQL_Project3","MySQL")

#Sqlite
# ta = tables()
# cols = columns(ta)
# print(cols)
# generate("2",ta,cols,"sqlite_Project2","sqlite")

# Postgre
ta = PostgreTable()
cols = PostgreColumns(ta)
print(cols)
generate(1,ta,cols,"PostgreSQL_Project2","PostgreSQL")

