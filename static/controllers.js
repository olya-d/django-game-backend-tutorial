var PlayerControllers = angular.module('PlayerControllers', []);

PlayerControllers.controller('PlayerCtrl', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.players = [];
    $scope.channel = 'players';

    $dragon.onReady(function() {
        $dragon.subscribe('player', $scope.channel).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
        });
        $dragon.getList('player').then(function(response) {
            $scope.players = response.data;
        });
    });

    $dragon.onChannelMessage(function(channels, message) {
        if (indexOf.call(channels, $scope.channel) > -1) {
            $scope.$apply(function() {
                $scope.dataMapper.mapData($scope.players, message);
            });
        }
    });

    var move = function(player, dx, dy) {
        player.position_x += dx;
        player.position_y += dy;
        $dragon.update('player', player);
    };

    $scope.moveRight = function(player) {
        move(player, 1, 0);
    };
    $scope.moveLeft = function(player) {
        move(player, 1, 0);
    };
    $scope.moveUp = function(player) {
        move(player, 0, 1);
    };
    $scope.moveDown = function(player) {
        move(player, 0, -1);
    };
}]);

