#include <iostream>
using namespace std;

class Student {
public:
    string name;
    int age;
    int rollNo;
    string branch;
    void display() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Roll No: " << rollNo << endl;
        cout << "Branch: " << branch << endl;
    }
};

int main() {
    cout << "Hello, World!" << endl;
    auto student1 = Student();
    student1.name = "John Doe";
    student1.age = 20;
    student1.rollNo = 1;
    student1.branch = "CSE";
    student1.display();
    
    return 0;
}