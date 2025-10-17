#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // 初始化随机数生成器
    srand(time(NULL));

    // 生成 1-99 的随机数
    int target = rand() % 99 + 1;
    int guess;
    int attempts = 0;

    printf("Guess an integer between 1 and 100 (100 is not included):\n");

    do {
        attempts++;

        // 读取用户输入
        if (scanf("%d", &guess) != 1) {
            printf("Please enter a valid number: ");
            // 清除输入缓冲区
            while (getchar() != '\n');
            continue;
        }

        // 比较猜测与目标数字
        if (guess < target) {
            printf("Too small! Try again: ");
        } else if (guess > target) {
            printf("Too big! Try again: ");
        } else {
            printf("You win! You tried %d times.\n", attempts);
            break;
        }
    } while (1);

    return 0;
}