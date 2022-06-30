from controller import controller

def view():
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hellow word</title>
</head>
<body>
    <h1>This a view for the store</h1>
    <h2>{controller()}</h2>
</body>
</html>
    """

if __name__ == "__main__": 
    print(view())