# -*- coding: utf-8 -*-

i = 3
head = '''
<!DOCTYPE html>
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
tail = '''
            </tbody>
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
</html>
'''

words = '''дом,复-á|房子
дóма[副]|在家里
вот[语]|这就是
вы|你们,您
вы́ставка|展览;展览会
суббóта|星期六
собáка|狗
су́мка|手提包
стакáн|杯子
банк|银行
бу́ква|字母
банáн|香蕉
космонáвт|宇航员
фóто[中，不变]|照片
кóфта|女短上衣
сад, 复-ы́|花园，果园
да[语气]|是的
фонтáн|喷泉
кафé[фэ́][中，不变]|咖啡馆,小吃店
автóбус|公共汽车
вуз|高等学校
ва́за|花瓶
по́вар, 复-а́|厨师
заво́д|工厂
за́втрак|早餐
зову́т(Как зову́т?)|叫(叫什么名字?)
му́зыка|音乐
музыка́нт|音乐家
когда́[副]|什么时候
пого́да|天气
нога́|脚,腿
газ|天然气
гора́|山
го́род, 复-а́|城市
бар|酒吧
спорт|体育
па́спорт, 复-а́|护照
торт|蛋糕
ра́но[副]|早
уро́к|功课,课
у́тро|早晨
у́тром[副]|在早晨
рабо́та|工作;作品
гру́ппа|班级;小组
друг|朋友
полру́га|女朋友
брат|兄弟
рука́|手
ры́нок|市场
вхол|入口
у́хо|耳朵
су́хо[副]|干燥
са́хар|糖
(он, она́, оно́) стои́т|(他,她,它)站立着
Дон|顿河
Москва́|莫斯科
Баку́|巴库(阿塞拜疆首都)'''
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
