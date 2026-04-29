/*** 
 * @Date: 2026-04-29 12:55:34
 */
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    for (const auto& n : numbers) {
        std::cout << n << " ";
    }
    return 0;
}