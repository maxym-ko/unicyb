#ifndef __GAME_H__
#define __GAME_H__

#include <SFML/Graphics.hpp>

#include <random>
#include <utility>
#include <vector>

enum class Direction {
    UP, RIGHT, DOWN, LEFT
};

class Game {
public:

    static void run();

private:

    static sf::RenderWindow *window;
    static int score;
    static bool alive;

    static std::pair<int, int> foodLocation;

    static const int range_x_from;
    static const int range_x_to;
    static std::random_device rand_devX;
    static std::mt19937 generatorX;
    static std::uniform_int_distribution<int> distribution_x;

    static const int range_y_from;
    static const int range_y_to;
    static std::random_device rand_devY;
    static std::mt19937 generatorY;
    static std::uniform_int_distribution<int> distribution_y;

    static std::vector<std::pair<int, int>> snake_body;
    static Direction snake_direction;
    static Direction new_direction;

    static std::pair<int, int> getNewFoodLocation();

    static void moveSnake();

    static void draw();

    static bool collides(std::pair<int, int>, const std::vector<std::pair<int, int>> &);

    static sf::Texture body;
    static sf::Texture food;

    static sf::Sprite body_spr;
    static sf::Sprite food_spr;
};

#endif
