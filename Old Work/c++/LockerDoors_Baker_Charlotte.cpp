#include <iostream>
#include <vector>

int main() {
    int n, r;
    
    std::cout << "Enter the number of locker doors: ";
    std::cin >> n;
    std::cout << "Enter the number of passes: ";
    std::cin >> r;

    // Initialize all lockers to closed (false)
    std::vector<bool> lockers(n, false);

    // Perform r passes
    for (int pass = 1; pass <= r; ++pass) {
        for (int i = pass - 1; i < n; i += pass) {
            lockers[i] = !lockers[i]; // Toggle the locker
        }
    }

    // Output locker status
    int openCount = 0;
    for (int i = 0; i < n; ++i) {
        std::cout << "Locker door #" << (i + 1) << ": " 
                  << (lockers[i] ? "open" : "closed") << std::endl;
        if (lockers[i]) ++openCount;
    }

    std::cout << "Total open lockers: " << openCount << std::endl;

    return 0;
}
