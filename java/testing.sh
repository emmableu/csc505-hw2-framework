#/usr/bin/sh
javac -cp .:junit-4.12.jar Solution.java SortingTest.java
java -cp .:junit-4.12.jar:hamcrest-core-1.3.jar org.junit.runner.JUnitCore SortingTest
