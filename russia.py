# -*- coding: utf-8 -*-
i = 4

word = ''

words = words.replace('!а','а́').replace('!е','е́').replace('!у','у́').replace('!и','и́').replace('!о','о́')
words = words.replace('!э','э́').replace('!ы','ы́').replace('!я','я́').replace('!ю','ю́')

head = '''<!DOCTYPE html>
<html lang="en">
   <head>
      <title>Russian Vocabulary</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
      <style>
         body {
            padding-top: 2em;
            background-color:#F8F8F8;
         }
         tr{
            background-color:white;
         }
      </style>
   </head>
   <body>
      <div class="container">
         <h3>第%d课</h3>
         <table class="table">
            <tbody>'''%i

tail = '''            </tbody>
         </table>
      </div>
   </body>
   <script>
      function m(f) {
         var win = new Audio(f);
         win.play();
      }
      $('table tr').each(function(a,b){
         $(b).click(function(){
            $('table tr').css('background','white');
            $(this).css('background','#E8E8E8');   
         });
      });
   </script>
</html>'''

words = words.split('\n')
print head
j = 1
for word in words:
  r,c = word.split('|')
  print '''               <tr onclick="m('L%02d/untitled-%02d.wav')">'''%(i,j)
  print '                  <td>%s</td>'%r
  print '                  <td>%s</td>'%c
  print '               </tr>'
  j += 1
print tail
