<?php
session_start();

try{
    $conn =new PDO("sqlite:S:/Projects/SeniorProject/Data.sqlite3");// the sqlite db path here need to be changed if needed
} catch (PDOException $e) {
    echo "<script>alert('Could not connect to the Database')</script>";
}

?>
<!DOCTYPE html>
<html>
    <head>
        <?php
            echo "<title>Select Look and feel of the page</title>";
        ?>

        <meta charset='utf-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>
        <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>
        <script src='https://code.jquery.com/jquery-3.3.1.slim.min.js' integrity='sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo' crossorigin='anonymous'></script>
        <script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js' integrity='sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1' crossorigin='anonymous'></script>
        <script src='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js' integrity='sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM' crossorigin='anonymous'></script>
        <link href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css' rel='stylesheet'/>
        
        <script type='text/javascript' src='https://drive.google.com/uc?id=1L1cVnuVbyf6r73eT0YUaTSxsFYy9a_IR'></script>
         <?php
            
            if(isset($_REQUEST["check"])){
                try{
                    $sql = "SELECT URL from Designs WHERE Sr=".$_GET["SelectedDesign"];
                    $getresult = $conn->query($sql);
                    $result = $getresult->fetch();
                    echo "<link rel='stylesheet' href='".$result["URL"]."'>";
                }catch(Exception $e){
                    echo "<script>alert('Failed to get the style')</script>";
                }
            }else{
                    echo "<link rel='stylesheet' href='https://drive.google.com/uc?id=1VA6zA6oHJXwBgcgnUc4lTOaCrx0TH0Fp'>";
            }
            if(isset($_REQUEST["setasdefault"])){
                try{
                    $sql = "update History set Design =".$_GET["SelectedDesign"]." WHERE PageName='".$_SESSION["PageName"]."' AND user='".$_SESSION["user"]."'";
                    $getresult = $conn->query($sql);
                }catch(Exception $e){
                    echo "<script>alert('Failed to set the style as default style')</script>";
                }
            }
         ?>

    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <?php
            if (!empty($_SESSION["PageName"])) {
                echo "<a href='".$_SESSION["PageName"].".php'><h1 id='logoh1' class= '= mr-sm-3'>".$_SESSION["PageName"]."</h1></a>";
            } else {
                echo "<h1 id='logoh1'>DB</h1>";
            }
            ?>

            <hr>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <?php
                        echo "<form class= 'form-inline my-2 my-lg-0'>";
                        echo"<li class= 'nav-item'>";
                        $sql = "SELECT * FROM Designs;";
                        $getresult = $conn->query($sql);

                        echo "<select name='SelectedDesign' class= 'form-control mr-sm-3' required>";
                        foreach($getresult as $row){
                            print($row["Name"]);
                        echo "<option value='".$row["Sr"]."'>".$row["Name"]."</option>";
                        }
                        echo "</select>";
                        echo"</li>";
                        echo"<li class= 'nav-item'>";
                        echo "<button class='btn btn-outline-success mr-sm-3 my-sm-0' name='check'  type='submit'>check</button>";
                        echo"</li>";
                        
                        echo"<li class= 'nav-item'>";
                        echo "<button class='btn btn-outline-success mr-sm-3 my-sm-0' name='setasdefault' type='submit'>Set as Default</button>";
                        echo"</li>";
                        
                        echo "</form>";
                     
                    ?>
                </ul>

            </div>
        </nav>

        <div class="container-fluid margin-top-1">
        </div>
        <div class="container-fluid mar ">
            <table id="allActivities">
                <?php
                    echo"<tr>";
                    echo"<th id=sr>Sr#</th>";
                    echo"<th id='name'>Username</th>";
                    echo"<th id='email'>Email</th>";
                    echo"<th id='status'>Status</th>";
                    echo"<th id='actions'>actions</th>";
                    echo"</tr>";
                    echo"<form>";
                    echo"<tr>";
                    echo"<td id='Sr'><input type='text' name='Sr'></td>";
                    echo"<td id='UserName'><input type='text' name='Username'></td>";
                    echo"<td id='Email'><input type='text' name='Email'></td>";
                    echo"<td id='Status'><input type='text' name='Status'></td>";
                    echo"<td><button name='add' type='button' class='btn AcceptBtn'>Add</button></td>";
                    echo"</tr>";
                    echo"</form>";
                ?>

            </table>
        </div>
        <footer>
            <div class="row">
                <div class="col-sm-2">
                    <img src="./images/KFUPMLogo.png" alt="Logo" width="250" height="250">
                </div>
                <div class="col-sm-2" id="copyrights">
                    <p>&copy; Murtada Alawami<br>Mohammed Al-Sayed</p>
                </div>
            </div>
        </footer>

    </body>
</html>