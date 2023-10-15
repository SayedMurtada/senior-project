<?php 
session_start();
if(empty($_SESSION['user'])){
   $_SESSION['user']='1';
}
if (!empty($_SESSION[''PathDB'])) {
    try{
        $conn =new PDO("sqlite:".        $_SESSION[''PathDB']);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $_SESSION[''Connected'] = 1;
    } catch (PDOException $e) {
        echo"<script>alert('Could not connect to the Database')</script>";
    }
}
$_SESSION['PageName']=''';
if (isset($_REQUEST['PageName'])) {
    $_SESSION["PageName"] = "'";
    echo'<meta http-equiv="refresh"content="0; URL=Copy.php" />';
}
if(empty($_SESSION[''Title'])) {
$_SESSION[''Title'] =''';
}
if(empty($_SESSION[''CurrentPage'])) {
$_SESSION[''CurrentPage'] = 'Designs';
}
if(isset($_REQUEST['Designs'])) {
    $_SESSION[''CurrentPage'] = $_REQUEST['Designs'];
}
if(isset($_REQUEST['sqlite_sequence'])) {
    $_SESSION[''CurrentPage'] = $_REQUEST['sqlite_sequence'];
}
?>
<!DOCTYPE html>
<html>
    <head>
        <?php
        if(!empty($_SESSION[''Title'])){
            echo"<title>".$_SESSION[''Title']."</title>";
        } else {
            echo'<title>Login</title>';
        }
        ?>
        <meta charset='utf-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>
        <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>
        <script src='https://code.jquery.com/jquery-3.3.1.slim.min.js' integrity='sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo' crossorigin='anonymous'></script>
        <script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js' integrity='sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1' crossorigin='anonymous'></script>
        <script src='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js' integrity='sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM' crossorigin='anonymous'></script>
        <?php
        if(!empty($_SESSION['sqlite_ProjectConnected'])){
            try{
                $conn2 =new PDO("sqlite:D:\KFUPM\192\ICS411\gui\Data.sqlite3");
                $sql = "SELECT Design FROM History WHERE PageName =''' and user='1'";
                $getresult = $conn2->query($sql);
                $result = $getresult->fetch();
                $sql = "SELECT URL FROM Designs WHERE Sr= '$result[0]'";
                $getresult = $conn2->query($sql);
                $result = $getresult->fetch();
                echo "<link rel='stylesheet' href='".$result[0]."'>";
            }catch(Exception $e){
                echo'<script>alert("could not get Style File")</script>';
            }
        }else{
                echo "<link rel='stylesheet' href='https://drive.google.com/uc?id=1VA6zA6oHJXwBgcgnUc4lTOaCrx0TH0Fp'>";
        }
        ?>
    </head>
    <body>
        <nav class='navbar navbar-expand-lg navbar-light bg-light'>
            <?php
            if ($_SESSION[''CurrentPage'] == 'Designs' && !empty($_SESSION[''Connected'])) {
                echo "<h1 id='logoh1'>Designs</h1>";
            }
            if ($_SESSION[''CurrentPage'] == 'sqlite_sequence' && !empty($_SESSION[''Connected'])) {
                echo "<h1 id='logoh1'>sqlite_sequence</h1>";
            }
            if(empty($_SESSION[''Connected'])){
                echo "<h1 id='logoh1'>DB</h1>";
            } 
            ?>
            <hr>
            <button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarSupportedContent' aria-controls='navbarSupportedContent' aria-expanded='false' aria-label='Toggle navigation'>
                <span class='navbar-toggler-icon'></span>
            </button>
            <div class='collapse navbar-collapse' id='navbarSupportedContent'>
                <ul class='navbar-nav mr-auto'>
                    <?php
                    if (!empty($_SESSION[''PathDB'])) {
                        echo"<li class= 'nav-item'>";
                        echo"<h1 id= 'logoh1'>Connected successfully</h1>";
                        echo"</li>";
                        echo"<form>";
                        echo"<li class= 'nav-item'>";
                        echo"<button class='btn btn-outline-success my-2 my-sm-3' name='PageName' value='MySQL_Project' type='submit'>Look and feel</button>";
                        echo"</li>";
                        echo"</form>";
                    } else {
                        echo"<form class='form-inline my-2 my-lg-0' method='post'>";
                        echo"<li class='nav-item'>";
                        echo"<input class='form-control mr-sm-2' name='Path' type='text' placeholder='Path with the filename and extension'>";
                        echo"</li>";
                        echo"<button class='btn btn-outline-success my-2 my-sm-0' name='Connect' type='search'>Connect</button>";
                        echo"</li>";
                        echo"</form>";
                    }
                    if (isset($_REQUEST['Connect'])) {
                        $input = !empty($_POST['Path']);
                        if ($input) {
                                try{
                                    $conn =new PDO("sqlite:".$_POST['Path']);
                                    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                                    $_SESSION[''PathDB'] = $_POST['Path'];
                                    $_SESSION[''Connected'] = 1;
                                    echo"<meta http-equiv='refresh' content='0; URL='.php' />";
                                } catch (PDOException $e) {
                                    echo"<script>alert('Could not connect to the Database')</script>";
                                }
                        } else {
                            echo"<script>alert('Could not connect to the Database')</script>";
                        }
                    }
                    ?>
                </ul>
            </div>
        </nav>
        <div class='container-fluid margin-top-1'>
            <?php
            if (!empty($_SESSION[''PathDB'])) {
                echo "<form class='form-inline my-2 my-lg-0'>";
                echo "<button name='Designs' value = Designs class='btn generate1'>Designs</button>";
                echo "<button name='sqlite_sequence' value = sqlite_sequence class='btn generate1'>sqlite_sequence</button>";
                echo "</form>";
            } else {
                echo "<h1 id='logoh1'>Please Connect to the Database to show the list of tables</h1>";
            }
            ?>
        </div>
        <div class='container-fluid mar'>
            <table id="allActivities">
                <?php
                if (!empty($conn)) {
                    echo "<div class='form-inline'>";
                    echo "<form class='form-inline' action='' method='GET' id='mysearch'>";
                    echo "<input class='form-control col-md-8' name='searchinput' type='search' placeholder='Search Activities' style='margin-left: 13%;'>";
                    echo "<button class='btn btn-outline-success my-2 my-sm-0' type='submit' name='Search'>Search</button>";
                    echo "<select name=reference>";
            if ($_SESSION[''CurrentPage'] == 'Designs') {
                echo "<option value='Sr'>Sr</option>";
                echo "<option value='Name'>Name</option>";
            }
            if ($_SESSION[''CurrentPage'] == 'sqlite_sequence') {
                echo "<option value='name'>name</option>";
                echo "<option value='seq'>seq</option>";
            }
                    echo "</select>";
                    echo "</form>";
                    echo "</div>";
        if (isset($_REQUEST['Search'])) {
            $input = $_GET['searchinput'];
            if (empty($input)) {
            if ($_SESSION[''CurrentPage'] == 'Designs') {
                echo"<tr>";
                echo"<th id='Sr'>Sr</th>";
                echo"<th id='Name'>Name</th>";
                echo"<th id=actions'>Actions</th>";
                echo"</tr>";
                echo"<form>";
                echo"<tr>";
                echo"<td id='Sr'><input type='text' name='Sr'></td>";
                echo"<td id='Name'><input type='text' name='Name'></td>";
                echo "<td><button name='add' type='submit' class='btn AcceptBtn'>Add</button></td>";
                echo"</tr>";
                echo"</form>";
                if (isset($_REQUEST['add'])) {
                     try{
                     $sqlgetStatus = "INSERT INTO Designs (Sr,Name) VALUES('" .$_GET["Sr"]."','".$_GET["Name"]."');";
                     $getStatus = $conn->exec($sqlgetStatus);
                     $conn = null;
                     echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                     }catch(Exception $e){
                         echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                     }
                }
                $sqlUsers = "SELECT Sr,Name FROM Designs;";
                $result = $conn->query($sqlUsers);
                if (!empty($result)) {
                    foreach ($result as $row) {
                        echo "<tr>";
                        echo "<form>";
                        echo "<td><input type='text' name='Sr' value='".$row["Sr"] ."'></td>";
                        echo "<td><input type='text' name='Name' value='".$row["Name"] ."'></td>";
                        $UserSr = $row['Name'];
                        echo "<td><button name='delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>";
                        echo "<button name='savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button></td>";
                        echo "</form>";
                        if (isset($_REQUEST['delete'])) {
                            try{
                            $sqlgetStatus = "DELETE FROM Designs WHERE Name ='". $_GET['delete'] ."';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                             }catch(Exception $e){
                                 $_REQUEST['delete']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                             }
                        } else if(isset($_REQUEST['savechanges'])){
                            try{
                            $PassedSr = $_GET['savechanges'];
                            $sqlgetStatus = "UPDATE Designs SET Sr='". $_GET['Sr'] ."',Name='". $_GET['Name'] ."' WHERE Name ='$PassedSr';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                             }catch(Exception $e){
                                 $_REQUEST['savechanges']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                             }
                        }
                        echo "</tr>";
                    }
                }
            }
            if ($_SESSION[''CurrentPage'] == 'sqlite_sequence') {
                echo"<tr>";
                echo"<th id='name'>name</th>";
                echo"<th id='seq'>seq</th>";
                echo"<th id=actions'>Actions</th>";
                echo"</tr>";
                echo"<form>";
                echo"<tr>";
                echo"<td id='name'><input type='text' name='name'></td>";
                echo"<td id='seq'><input type='text' name='seq'></td>";
                echo "<td><button name='add' type='submit' class='btn AcceptBtn'>Add</button></td>";
                echo"</tr>";
                echo"</form>";
                if (isset($_REQUEST['add'])) {
                     try{
                     $sqlgetStatus = "INSERT INTO sqlite_sequence (name,seq) VALUES('" .$_GET["name"]."','".$_GET["seq"]."');";
                     $getStatus = $conn->exec($sqlgetStatus);
                     $conn = null;
                     echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                     }catch(Exception $e){
                         echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                     }
                }
                $sqlUsers = "SELECT name,seq FROM sqlite_sequence;";
                $result = $conn->query($sqlUsers);
                if (!empty($result)) {
                    foreach ($result as $row) {
                        echo "<tr>";
                        echo "<form>";
                        echo "<td><input type='text' name='name' value='".$row["name"] ."'></td>";
                        echo "<td><input type='text' name='seq' value='".$row["seq"] ."'></td>";
                        $UserSr = $row['seq'];
                        echo "<td><button name='delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>";
                        echo "<button name='savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button></td>";
                        echo "</form>";
                        if (isset($_REQUEST['delete'])) {
                            try{
                            $sqlgetStatus = "DELETE FROM sqlite_sequence WHERE seq ='". $_GET['delete'] ."';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                             }catch(Exception $e){
                                 $_REQUEST['delete']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                             }
                        } else if(isset($_REQUEST['savechanges'])){
                            try{
                            $PassedSr = $_GET['savechanges'];
                            $sqlgetStatus = "UPDATE sqlite_sequence SET name='". $_GET['name'] ."',seq='". $_GET['seq'] ."' WHERE seq ='$PassedSr';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                             }catch(Exception $e){
                                 $_REQUEST['savechanges']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                             }
                        }
                        echo "</tr>";
                    }
                }
            }
            } else {
                if (empty(preg_replace('/\s+/', '', $input))) {
            if ($_SESSION[''CurrentPage'] == 'Designs') {
                echo"<tr>";
                echo"<th id='Sr'>Sr</th>";
                echo"<th id='Name'>Name</th>";
                echo"<th id=actions'>Actions</th>";
                echo"</tr>";
                echo"<form>";
                echo"<tr>";
                echo"<td id='Sr'><input type='text' name='Sr'></td>";
                echo"<td id='Name'><input type='text' name='Name'></td>";
                echo "<td><button name='add' type='submit' class='btn AcceptBtn'>Add</button></td>";
                echo"</tr>";
                echo"</form>";
                if (isset($_REQUEST['add'])) {
                     try{
                     $sqlgetStatus = "INSERT INTO Designs (Sr,Name) VALUES('" .$_GET["Sr"]."','".$_GET["Name"]."');";
                     $getStatus = $conn->exec($sqlgetStatus);
                     $conn = null;
                     echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                     }catch(Exception $e){
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                     }
                }
                $sqlUsers = "SELECT Sr,Name FROM Designs;";
                $result = $conn->query($sqlUsers);
                if (!empty($result)) {
                    foreach ($result as $row) {
                        echo "<tr>";
                        echo "<form>";
                        echo "<td><input type='text' name='Sr' value='".$row["Sr"] ."'></td>";
                        echo "<td><input type='text' name='Name' value='".$row["Name"] ."'></td>";
                        $UserSr = $row['Name'];
                        echo "<td><button name='delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>";
                        echo "<button name='savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button></td>";
                        echo "</form>";
                        if (isset($_REQUEST['delete'])) {
                            try{
                            $sqlgetStatus = "DELETE FROM Designs WHERE Name ='". $_GET['delete'] ."';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                            }catch(Exception $e){
                                 $_REQUEST['delete']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        } else if(isset($_REQUEST['savechanges'])){
                            try{
                            $PassedSr = $_GET['savechanges'];
                            $sqlgetStatus = "UPDATE Designs SET Sr='". $_GET['Sr'] ."',Name='". $_GET['Name'] ."' WHERE Name ='$PassedSr';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                            }catch(Exception $e){
                                 $_REQUEST['savechanges']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        }
                        echo "</tr>";
                    }
                }
            }
            if ($_SESSION[''CurrentPage'] == 'sqlite_sequence') {
                echo"<tr>";
                echo"<th id='name'>name</th>";
                echo"<th id='seq'>seq</th>";
                echo"<th id=actions'>Actions</th>";
                echo"</tr>";
                echo"<form>";
                echo"<tr>";
                echo"<td id='name'><input type='text' name='name'></td>";
                echo"<td id='seq'><input type='text' name='seq'></td>";
                echo "<td><button name='add' type='submit' class='btn AcceptBtn'>Add</button></td>";
                echo"</tr>";
                echo"</form>";
                if (isset($_REQUEST['add'])) {
                     try{
                     $sqlgetStatus = "INSERT INTO sqlite_sequence (name,seq) VALUES('" .$_GET["name"]."','".$_GET["seq"]."');";
                     $getStatus = $conn->exec($sqlgetStatus);
                     $conn = null;
                     echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                     }catch(Exception $e){
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                     }
                }
                $sqlUsers = "SELECT name,seq FROM sqlite_sequence;";
                $result = $conn->query($sqlUsers);
                if (!empty($result)) {
                    foreach ($result as $row) {
                        echo "<tr>";
                        echo "<form>";
                        echo "<td><input type='text' name='name' value='".$row["name"] ."'></td>";
                        echo "<td><input type='text' name='seq' value='".$row["seq"] ."'></td>";
                        $UserSr = $row['seq'];
                        echo "<td><button name='delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>";
                        echo "<button name='savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button></td>";
                        echo "</form>";
                        if (isset($_REQUEST['delete'])) {
                            try{
                            $sqlgetStatus = "DELETE FROM sqlite_sequence WHERE seq ='". $_GET['delete'] ."';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                            }catch(Exception $e){
                                 $_REQUEST['delete']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        } else if(isset($_REQUEST['savechanges'])){
                            try{
                            $PassedSr = $_GET['savechanges'];
                            $sqlgetStatus = "UPDATE sqlite_sequence SET name='". $_GET['name'] ."',seq='". $_GET['seq'] ."' WHERE seq ='$PassedSr';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                            }catch(Exception $e){
                                 $_REQUEST['savechanges']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        }
                        echo "</tr>";
                    }
                }
            }
                }else {
            if ($_SESSION[''CurrentPage'] == 'Designs') {
                echo"<tr>";
                echo"<th id='Sr'>Sr</th>";
                echo"<th id='Name'>Name</th>";
                echo"<th id=actions'>Actions</th>";
                echo"</tr>";
                echo"<form>";
                echo"<tr>";
                echo"<td id='Sr'><input type='text' name='Sr'></td>";
                echo"<td id='Name'><input type='text' name='Name'></td>";
                echo "<td><button name='add' type='submit' class='btn AcceptBtn'>Add</button></td>";
                echo"</tr>";
                echo"</form>";
                if (isset($_REQUEST['add'])) {
                     try{
                     $sqlgetStatus = "INSERT INTO Designs (Sr,Name) VALUES('" .$_GET["Sr"]."','".$_GET["Name"]."');";
                     $getStatus = $conn->exec($sqlgetStatus);
                     $conn = null;
                     echo '<meta http-equiv= "refresh" content="0; URL='.php" />';
                     }catch(Exception $e){
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                     }
                }
                $sqlUsers = "SELECT Sr,Name FROM Designs WHERE " . $_GET["reference"] ." ='". $_GET["searchinput"] ."'";
                $result = $conn->query($sqlUsers);
                if (!empty($result)) {
                    foreach ($result as $row) {
                        echo "<tr>";
                        echo "<form>";
                        echo "<td><input type='text' name='Sr' value='".$row["Sr"] ."'></td>";
                        echo "<td><input type='text' name='Name' value='".$row["Name"] ."'></td>";
                        $UserSr = $row['Name'];
                        echo "<td><button name='delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>";
                        echo "<button name='savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button></td>";
                        echo "</form>";
                        if (isset($_REQUEST['delete'])) {
                            try{
                            $sqlgetStatus = "DELETE FROM Designs WHERE Name = ' " . $_GET['delete'] . " '; ";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                            }catch(Exception $e){
                                 $_REQUEST['delete']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        } else if(isset($_REQUEST['savechanges'])){
                            try{
                            $PassedSr = $_GET['savechanges'];
                            $sqlgetStatus = "UPDATE Designs SET Sr='". $_GET['Sr'] ."',Name='". $_GET['Name'] ."' WHERE Name ='$PassedSr';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv= "refresh" content="0; URL='.php" />';
                            }catch(Exception $e){
                                 $_REQUEST['savechanges']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        }
                        echo "</tr>";
                    }
                }
            }
            if ($_SESSION[''CurrentPage'] == 'sqlite_sequence') {
                echo"<tr>";
                echo"<th id='name'>name</th>";
                echo"<th id='seq'>seq</th>";
                echo"<th id=actions'>Actions</th>";
                echo"</tr>";
                echo"<form>";
                echo"<tr>";
                echo"<td id='name'><input type='text' name='name'></td>";
                echo"<td id='seq'><input type='text' name='seq'></td>";
                echo "<td><button name='add' type='submit' class='btn AcceptBtn'>Add</button></td>";
                echo"</tr>";
                echo"</form>";
                if (isset($_REQUEST['add'])) {
                     try{
                     $sqlgetStatus = "INSERT INTO sqlite_sequence (name,seq) VALUES('" .$_GET["name"]."','".$_GET["seq"]."');";
                     $getStatus = $conn->exec($sqlgetStatus);
                     $conn = null;
                     echo '<meta http-equiv= "refresh" content="0; URL='.php" />';
                     }catch(Exception $e){
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                     }
                }
                $sqlUsers = "SELECT name,seq FROM sqlite_sequence WHERE " . $_GET["reference"] ." ='". $_GET["searchinput"] ."'";
                $result = $conn->query($sqlUsers);
                if (!empty($result)) {
                    foreach ($result as $row) {
                        echo "<tr>";
                        echo "<form>";
                        echo "<td><input type='text' name='name' value='".$row["name"] ."'></td>";
                        echo "<td><input type='text' name='seq' value='".$row["seq"] ."'></td>";
                        $UserSr = $row['seq'];
                        echo "<td><button name='delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>";
                        echo "<button name='savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button></td>";
                        echo "</form>";
                        if (isset($_REQUEST['delete'])) {
                            try{
                            $sqlgetStatus = "DELETE FROM sqlite_sequence WHERE seq = ' " . $_GET['delete'] . " '; ";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                            }catch(Exception $e){
                                 $_REQUEST['delete']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        } else if(isset($_REQUEST['savechanges'])){
                            try{
                            $PassedSr = $_GET['savechanges'];
                            $sqlgetStatus = "UPDATE sqlite_sequence SET name='". $_GET['name'] ."',seq='". $_GET['seq'] ."' WHERE seq ='$PassedSr';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv= "refresh" content="0; URL='.php" />';
                            }catch(Exception $e){
                                 $_REQUEST['savechanges']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        }
                        echo "</tr>";
                    }
                }
            }
                }
            }
        } else {
            if ($_SESSION[''CurrentPage'] == 'Designs') {
                echo"<tr>";
                echo"<th id= 'Sr'>Sr</th>";
                echo"<th id= 'Name'>Name</th>";
                echo"<th id=actions'>Actions</th>";
                echo"</tr>";
                echo"<tr>";
                echo"<form>";
                echo"<td id='Sr'><input type='text' name='Sr'></td>";
                echo"<td id='Name'><input type='text' name='Name'></td>";
                echo "<td><button name='add' type='submit' class='btn AcceptBtn'>Add</button></td>";
                echo"</form>";
                echo"</tr>";
                if (isset($_REQUEST['add'])) {
                     try{
                     $sqlgetStatus = "INSERT INTO Designs (Sr,Name) VALUES('" .$_GET["Sr"]."','".$_GET["Name"]."');";
                     $getStatus = $conn->exec($sqlgetStatus);
                     $conn = null;
                     echo '<meta http-equiv= "refresh" content="0; URL='.php"/>';
                     }catch(Exception $e){
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                     }
                }
                $sqlUsers = "SELECT Sr,Name FROM Designs;";
                $result = $conn->query($sqlUsers);
                if (!empty($result)) {
                    foreach ($result as $row) {
                        echo "<tr>";
                        echo "<form>";
                        echo "<td><input type='text' name='Sr' value='".$row["Sr"] ."'></td>";
                        echo "<td><input type='text' name='Name' value='".$row["Name"] ."'></td>";
                        $UserSr = $row['Name'];
                        echo "<td><button name='delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>";
                        echo "<button name='savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button></td>";
                        echo "</form>";
                        if (isset($_REQUEST['delete'])) {
                            try{
                            $sqlgetStatus = "DELETE FROM Designs WHERE Name = ' ". $_GET['delete'] . " ';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv= "refresh" content="0; URL='.php"/>';
                            }catch(Exception $e){
                                 $_REQUEST['delete']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        } else if(isset($_REQUEST['savechanges'])){
                            try{
                            $PassedSr = $_GET['savechanges'];
                            $sqlgetStatus = "UPDATE Designs SET Sr='". $_GET['Sr'] ."',Name='". $_GET['Name'] ."' WHERE Name ='$PassedSr';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                            }catch(Exception $e){
                                 $_REQUEST['savechanges']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        }
                        echo "</tr>";
                    }
                }
            }
            if ($_SESSION[''CurrentPage'] == 'sqlite_sequence') {
                echo"<tr>";
                echo"<th id= 'name'>name</th>";
                echo"<th id= 'seq'>seq</th>";
                echo"<th id=actions'>Actions</th>";
                echo"</tr>";
                echo"<tr>";
                echo"<form>";
                echo"<td id='name'><input type='text' name='name'></td>";
                echo"<td id='seq'><input type='text' name='seq'></td>";
                echo "<td><button name='add' type='submit' class='btn AcceptBtn'>Add</button></td>";
                echo"</form>";
                echo"</tr>";
                if (isset($_REQUEST['add'])) {
                     try{
                     $sqlgetStatus = "INSERT INTO sqlite_sequence (name,seq) VALUES('" .$_GET["name"]."','".$_GET["seq"]."');";
                     $getStatus = $conn->exec($sqlgetStatus);
                     $conn = null;
                     echo '<meta http-equiv= "refresh" content="0; URL='.php"/>';
                     }catch(Exception $e){
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                     }
                }
                $sqlUsers = "SELECT name,seq FROM sqlite_sequence;";
                $result = $conn->query($sqlUsers);
                if (!empty($result)) {
                    foreach ($result as $row) {
                        echo "<tr>";
                        echo "<form>";
                        echo "<td><input type='text' name='name' value='".$row["name"] ."'></td>";
                        echo "<td><input type='text' name='seq' value='".$row["seq"] ."'></td>";
                        $UserSr = $row['seq'];
                        echo "<td><button name='delete' type='submit' value ='$UserSr' class='btn reject'>Delete</button>";
                        echo "<button name='savechanges' type='submit' value ='$UserSr' class='btn block'>Save Changes</button></td>";
                        echo "</form>";
                        if (isset($_REQUEST['delete'])) {
                            try{
                            $sqlgetStatus = "DELETE FROM sqlite_sequence WHERE seq = ' ". $_GET['delete'] . " ';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv= "refresh" content="0; URL='.php"/>';
                            }catch(Exception $e){
                                 $_REQUEST['delete']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        } else if(isset($_REQUEST['savechanges'])){
                            try{
                            $PassedSr = $_GET['savechanges'];
                            $sqlgetStatus = "UPDATE sqlite_sequence SET name='". $_GET['name'] ."',seq='". $_GET['seq'] ."' WHERE seq ='$PassedSr';";
                            $conn->exec($sqlgetStatus);
                            $conn = null;
                            echo '<meta http-equiv="refresh" content="0; URL='.php"/>';
                            }catch(Exception $e){
                                 $_REQUEST['savechanges']=null;
                                 echo'<script type="text/javascript">confirm("'.$e->getMessage().'");</script>';
                            }
                        }
                        echo "</tr>";
                    }
                }
            }
        }
                }
                ?>
            </table>
        </div>
        <footer>
            <div class='row'>
                <div class='col-sm-2'>
                    <img src='./images/KFUPMLogo.png' alt='Logo' width='250' height='250'>
                </div>
                <div class = 'col-sm-2' id = 'copyrights'>
                    <p>&copy; Murtada Alawami<br>Mohammed Al-Sayed</p>
                </div>
            </div>
        </footer>
    </body>
</html>