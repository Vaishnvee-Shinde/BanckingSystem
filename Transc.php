<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Online Online Bank Serivicek Serivice</title>
<style>
.button {
      background-color: #2b67f8; 
      border-radius: 29px;
    border-bottom-color:red;
      color: white;
      padding: 10px 25px;
      text-align: center;
      text-decoration:none;
      display: inline-block;
      font-size: 20px;
    }
     .header {
    margin-left: -2px;
    color: #243e83;
    font-size: 61px;
    font-variant: small-caps;
    margin-top: -140px;
}
    .button:hover {background-color: #1844aa}
    
    .button:active {
      background-color: #1844aa;
      box-shadow: 0 5px #666;
      transform: translateY(4px);
    }
            
    .topnav {
  overflow: hidden;
 
}
.btnstyle{
  padding-left: 7rem;
  padding-top: 34px;
}


.topnav {
  overflow: hidden;
  background-color: white;
}

.topnav a {
  float: left;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #2b67f8;
  color: white;
}

.topnav a.active {
  background-color: #2b67f8;
  color: white;
}

.topnav-right {
  float: right;
}
 .header {
    margin-left: -2px;
    color: #243e83;
    font-size: 61px;
    font-variant: small-caps;
    margin-top: -140px;
}
header a{
  text-decoration: none;
}
.tablediv{
  float: center;
  padding: 8px;
  margin:5px;
  width:70%; 
 margin-left:15%; 
margin-right:15%;
overflow-x:auto;
}
table{
  
  font-family:'Trebuchet MS',sans-serif;
  font-weight:bold;
  padding:5px;
  margin:1px;
   width: 100%;  
  border:1px solid white;
  border-collapse: collapse;
}
th{
  padding: 10px 10px;
  text-align: left;
  font-weight: 500;
  font-size: 20px;
  color: navy;
  text-transform: uppercase;
}
td{
  padding: 8px;
  text-align: left;
  vertical-align:middle;
  font-weight: bold;
  font-size: 18px;
  color: black;
  
}
@media screen and (max-width: 800px){
    
  body{
  background-size:cover;
  background-position: right;

}
    div.tablediv{
        width:100%; 
        margin-left:0%; 
        margin-right:0%;
        padding:0px;
        margin:0px;
        }
     table{
         padding:0px;
         margin:0px;
     } 
} 
@media screen and (max-width: 600px) {
  .topnav a:not(:first-child) {
    display: none;
  }
  .topnav a.icon {
    float: right;
    display: block;
  }
  
}

@media screen and (max-width: 400px) {
  .topnav.responsive {position: relative;}
  .topnav.responsive .icon {
    position: absolute;
    right: 0;
    top: 0;
  }
  .topnav.responsive a {
    float: none;
    display: block;
    text-align: left;
  }
  .topnav.responsive .dropdown {float: none;}
  .topnav.responsive .dropdown-content {position: relative;}
  .topnav.responsive .dropdown .dropbtn {
    display: block;
    width: 100%;
    text-align: left;
  }
}
</style>
</head>
<body>
<header> 
 <div class="topnav">
    <div class="topnav-right">
        <a href="index.html"  >Home</a>
        <a  href="View.php">View Customers</a>
        <a class="active" href="transc.php">View Transactions</a>
  </div>
</div>

<div class="header">
<h5 style="padding-right: 1rem">Online Bank Serivice</h5>
</div>
<script>
<script>
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
</script>

<div class="tablediv"> 
<br><br>
<table>
<tr>
<th>Sender Name</th>
<th>Sender A/c No.</th>
<th>Recipient Name</th>
<th>Recipient A/c No.</th>
<th>Amount</th>
<th>Date & Time</th>
</tr>
<?php
$conn = mysqli_connect("localhost", "root", "", "qxp");
// Check connection
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}
$sql = "SELECT * FROM transfer";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
// output data of each row
while($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<form method ='post' action = 'OneCustomer.php'>";
    echo "<td>" . $row["s_name"]. "</td><td>" . $row["s_acc_no"] . "</td><td>" . $row["r_name"]. "</td><td>" . $row["r_acc_no"] . "</td><td>" . $row["amount"] . "</td><td>" . $row["date_time"] . "</td>";
    echo "</tr>";
}
echo "</table>";
} else { echo "0 results"; }
$conn->close();
?>
</table>
</div>
</body>
</html>

