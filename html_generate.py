# -*- coding: utf-8 -*-
import os


def search_folder_with_script():
    directory = os.path.dirname(os.path.abspath(__file__))
    print directory
    current_folder = ''
    for i in directory:
        if i == '\\':
            current_folder = ''
        else:
            current_folder = current_folder + i
    return current_folder


def paste_images_in_folder():
    files = os.listdir(os.path.dirname(os.path.abspath(__file__)))
    images = filter(lambda x: x.endswith('.JPG'), files)
    for i in images:
        AlbumHtmlFile.write('                       <article> \n'
                            '                           <a class="thumbnail"'
                            'href="images/fulls/' + i + '.jpg"'
                            ' data-position="left center"> '
                            '<img src="images/thumbs/' + i + '.jpg"'
                            ' alt="' + i + '" /></a> \n' +
                            '<h2>Владимир Протас</h2> \n' +
                            '<p>' + i + '</p> \n'
                            '                       </article> \n')


AlbumHtmlFile = open('index.html', 'w')
AlbumHtmlFile.write('<!DOCTYPE HTML> \n' +
                    '<!-- \n' +
                    '   Lens by HTML5 UP \n' +
                    '   html5up.net | @n33co \n' +
                    '   Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)\n' +
                    '--> \n' +
                    '<html> \n' +
                    '   <head> \n' +
                    '       <title>' +
                    search_folder_with_script() +
                    ' | Vladimir Protas - famous Ukrainian sculptor </title> \n' +
                    '       <meta charset="utf-8" /> \n' +
                    '       meta name="viewport" content="width=device-width, initial-scale=1" /> \n' +
                    '       <!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]--> \n' +
                    '       <link rel="stylesheet" href="assets/css/main.css" /> \n' +
                    '       <!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]--> \n' +
                    '       <!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]--> \n' +
                    '       <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript> \n' +
                    '   </head> \n' +
                    '   <body class="is-loading-0 is-loading-1 is-loading-2"> \n' +
                    '\n' +
                    '       <!-- Main --> \n' +
                    '           <div id="main"> \n' +
                    '\n' +
                    '               <!-- Header --> \n' +
                    '                   <header id="header"> \n' +
                    '                       <h1>' +
                    search_folder_with_script() +
                    '</h1> \n' +
                    '                       <p><a href="../cv-rus.html" target="_blank">Про меня</a> |'
                    '<a href="../cv.html" target="_blank">About me</a>  |'
                    '<noindex>'
                    '<a href="http://www.facebook.com/profile.php?id=100002194797317" target="_blank" rel="nofollow">Facebook Profile</a> |'
                    ' <a href="http://www.facebook.com/home.php?sk=group_198239200217172" target="_blank" rel="nofollow">Facebook Group</a> |'
                    '<a href="../index.html" target="_blank">На главную</a> </p> \n' +
                    '                   </header> \n' +
                    '               <!-- Thumbnail -->\n' +
                    '                   <section id="thumbnails">\n')
paste_images_in_folder()
AlbumHtmlFile.write('                   </section> \n'
                    '               <!-- Footer --> \n'
                    '                   <footer id="footer"> \n'
                    '                       <ul class="copyright"> \n'
                    '                           <li>Copyright Protas V.N. &copy; 2010-2017</li></li> \n'
                    '                       </ul> \n'
                    '                   </footer> \n \n'
                    '           </div> \n \n'
                    '           <!-- hit.ua --> \n'
                    '''           <a href='http://hit.ua/?x=68914' target='_blank'> \n'''
                    '           <script language="javascript" type="text/javascript"><!-- \n'
                    '           Cd=document;Cr="&"+Math.random();Cp="&s=1"; \n'
                    '           Cd.cookie="b=b";if(Cd.cookie)Cp+="&c=1"; \n'
                    '           Cp+="&t="+(new Date()).getTimezoneOffset(); \n'
                    '			if(self!=top)Cp+="&f=1"; \n'
                    '           //--></script> \n'
                    '           <script language="javascript1.1" type="text/javascript"><!-- \n'
                    '           if(navigator.javaEnabled())Cp+="&j=1";\n'
                    '           //--></script> \n'
                    '           <script language="javascript1.2" type="text/javascript"><!--\n'
                    '           if(typeof(screen)!='"'undefined'"')Cp+="&w="+screen.width+"&h="+ \n'
                    '           screen.height+"&d="+(screen.colorDepth?screen.colorDepth:screen.pixelDepth); \n'
                    '           //--></script> \n'
                    '           <script language="javascript" type="text/javascript"><!-- \n'
                    '''           Cd.write("<img src='http://c.hit.ua/hit?i=68914&g=0&x=2"+Cp+Cr+
           "&r=" + escape(Cd.referrer) + "&u=" + escape(window.location.href) +
           "' border='0' wi"+"dth='1' he"+"ight='1'/>");
           //--></script>
           <noscript><img src='http://c.hit.ua/hit?i=68914&amp;g=0&amp;x=2' border='0'/>

           </noscript></a>
           <!-- / hit.ua -->'''
                    '       <!-- Scripts --> \n'
                    '           <script src="assets/js/jquery.min.js"></script> \n'
                    '           <script src="assets/js/skel.min.js"></script> \n'
                    '           <!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]--> \n'
                    '           <script src="assets/js/main.js"></script> \n'
                    '       </body> \n'
                    '</html>')
AlbumHtmlFile.close()
print locale.getlocale()
