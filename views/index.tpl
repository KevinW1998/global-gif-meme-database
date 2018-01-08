<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The global GIF Database</title>

    <!-- EASY Styling -->
    <style type="text/css">
        table {
            border-collapse: collapse;
        }

        table, th, td {
            border: 1px solid black;
        }
    </style>
</head>
<body>


<table style="border: 1px solid black">
    <tr>
        <th>Name</th>
        <th>Preview</th>
        <th>Link</th>
    </tr>
    % for meme in memes:
    <tr>
        <td>Image {{meme[0]}}</td>
        <td><img width="100" height="100" alt="{{meme[0]}}" src="{{meme[1]}}"></td>
        <td><a href="/view_gif/{{meme[0]}}">Full link</a></td>
    </tr>
    % end
</table>

<br>
<hr>
<form action="/upload_gif" method="post" enctype="multipart/form-data">
  Select a file: <input type="file" name="upload" accept="image/*"><br>
  <input type="submit" value="Start upload">
</form>

</body>
</html>