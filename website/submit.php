<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<html lang="en">

<head>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet">
</head>

<body>
    <div>
        <title>🔔 Covid-19 Updates</title>
        <h1 class="title"> Sign up for daily updates on COVID-19</h1>
    </div>
    <div>
        <?PHP
        $user_name = $_POST['name'];
        $user_email = $_POST['email'];
        $user_phone = $_POST['phone'];
        if (empty($user_name)) {
            $user_name = 'user';
        }
        if (empty($user_email)) {
            $user_email = 'na';
        }
        if (empty($user_phone)) {
            $user_phone = 'na';
        }
        echo "<p>Name: </p>";
        echo "<p class='output'>$user_name</p>";
        echo "<p>Delivery option: </p>";
        echo "<p class='output'>$_POST[type]</p>";
        echo "<p>Email: </p>";
        echo "<p class='output'>$user_email</p>";
        echo "<p>Phone: </p>";
        echo "<p class='output'>$user_phone</p>";
        echo "<p>Country: </p>";
        echo "<p class='output'>$_POST[country]</p>";
        ?>

        <p>
            Result:
        </p>
        <p class="result">
            <?PHP
            //# sys.argv[0] file path
            //# sys.argv[1] name
            //# sys.argv[2] delivery option
            //# sys.argv[3] country
            //# sys.argv[4] email
            //# sys.argv[5] phone
            //echo "//shell_exec disabled for testing//";
            echo shell_exec("python3 /stuff/hook.py '$user_name' '$_POST[type]' '$_POST[country]' '$user_email' '$user_phone' ");
            ?>
        </p>

    </div>
    <div class="footer">
        <p class="credit">made by (link to repo!)</p>
        <a class="s" href="https://github.com/seo-chang">Seo Chang</a>
        <a class="j" href="https://git.jaeha.dev/explorer">Jaeha Choi</a>
        <a class="d" href="https://github.com/dspani">Duncan Spani</a>
    </div>
</body>

</html>