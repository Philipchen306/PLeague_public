package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class TestDatabaseConnection {
    public static void main(String[] args) {
        String url = "jdbc:mysql://127.0.0.1:3307/pleague";
        String username = "root";
        String password = "12345678";

        try (Connection connection = DriverManager.getConnection(url, username, password)) {
            if (connection != null) {
                System.out.println("Connected to the database!");
            } else {
                System.out.println("Failed to make connection!");
            }
        } catch (SQLException e) {
            System.out.println("MySQL Connection Failed!");
            e.printStackTrace();
        }
    }
}


// cd /Users/a88693/Documents/PLeague/BackendJava/src/main/java/com/example
// javac -cp .:src/test/java:/path/to/mysql-connector-java-8.0.32.jar src/test/java/com/example/pleague/TestDatabaseConnection.java
