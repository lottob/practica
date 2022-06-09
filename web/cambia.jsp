<%-- 
    Document   : cambia
    Created on : 8/06/2021, 03:32:05 PM
    Author     : asus
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
       
        <script>
            
        var color = document.getElementById("color").innerHTML;
      
        
      </script>
        
    </head>
    
    <body >
        
       <%
           
       String nom = request.getParameter("nombre");
       String color = request.getParameter("letra");
       String fondo = request.getParameter("fondo");
       
       %>
       <div style="background-color: <%= fondo %>">
       <h1 style="font-size: 50px; color: white">Datos Recibidos!! </h1>
       <h1 style="color: <%= color %>; font-size: 100px" > <%= nom %> </h1>
       
       </div>
    </body>
</html>
