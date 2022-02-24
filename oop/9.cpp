#include <bits/stdc++.h>
using namespace std;

int main () {
  string firstName, lastName;
  const char* firstinitial, lastinitial;
  const char* initials[3];
  initials[3] = "A.A.";
  cout << initials[3];

  cout << "Enter First Name." << endl;
  getline (cin, firstName);
  cout << "Enter Last Name." << endl;
  getline (cin, lastName);

  firstinitial = firstName[0];
  lastinitial = lastName[0];

  cout << firstinitial << endl;
  cout << lastinitial << endl;

  initials[0] = firstinitial;
  //initials[0] = firstName[0];
  //initials[1] = ".";
  initials[2] = lastinitial;
  //initials[2] = lastName[0];
  //initials[3] = ".";

  cout << initials[3] << endl;

  return 0;
}