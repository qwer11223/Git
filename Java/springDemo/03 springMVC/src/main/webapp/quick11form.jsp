<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2022/2/10
  Time: 15:57
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    <form action="${pageContext.request.contextPath}/quick11">
        userList[0].name<input type="text" name="userList[0].name"><br/>
        userList[0].age<input type="text" name="userList[0].age"><br/>
        userList[1].name<input type="text" name="userList[1].name"><br/>
        userList[1].age<input type="text" name="userList[1].age"><br/>
        <input type="submit" value="submit">
    </form>
</body>
</html>
