<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The global GIF Database</title>


    <!-- EASY Styling -->
    <!--
    <style type="text/css">
        table {
            border-collapse: collapse;
        }

        table, th, td {
            border: 1px solid black;
        }
    </style>
    -->

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>

</head>
<body>
<div class="collapse bg-inverse" id="navbarHeader">
      <div class="container">
        <div class="row">
          <div class="col-sm-8 py-4">
            <h4 class="text-white">About</h4>
            <h5 class="text-muted">This is a completely useless drop-down menue :)</h5><br>
            <h5 class="text-muted">But you are amazed by the gui aren't you? ... Thank us with a "sehr gut"</h5>
          </div>
          <div class="col-sm-4 py-4">
            <h4 class="text-white">Contact</h4>
            <ul class="list-unstyled">
              <li><a href="#" class="text-white">dsunaric@student.tgm.ac.at</a></li>
              <li><a href="#" class="text-white">kwaldock@student.tgm.ac.at</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="navbar navbar-inverse bg-inverse">
      <div class="container d-flex justify-content-between">
        <a href="#" class="navbar-brand">Memes</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
    </div>

    <section class="jumbotron text-center">
      <div class="container">
        <h1 class="jumbotron-heading">Welcome to the new IT meme page</h1>
        <p class="lead text-muted">This is the new sick meme page ! Select a meme and upload it
            <form action="/upload_gif" method="post" enctype="multipart/form-data">
              <input type="file" name="upload" class="btn btn-primary" accept="image/*" style="width:200;height:100">
              <input type="submit" value="Start upload" class="btn btn-secondary" style="width:200;height:100">
            </form>

        </p>
      </div>
    </section>

    <div class="album text-muted">
      <div class="container">

        <div class="row">
            % for meme in memes:
          <div class="card" >
            <img  width="350"  alt="{{meme[0]}}" src="{{meme[1]}}" class="rounded img-thumbnail" >
            <div class="card-block">
                <h6 class="card-title">Image {{meme[0]}}</h6>
                <a href="#" class="btn btn-primary">Go somewhere</a>
              </div>
          </div>

            % end

        </div>

      </div>
    </div>


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
    %end
</table>

<br>
<hr>

</body>
</html>