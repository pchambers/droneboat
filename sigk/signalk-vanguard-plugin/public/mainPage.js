'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var MainPage = function (_React$Component) {
  _inherits(MainPage, _React$Component);

  function MainPage(props) {
    _classCallCheck(this, MainPage);

    // Setup the React "state" object used by this page...
    var _this = _possibleConstructorReturn(this, (MainPage.__proto__ || Object.getPrototypeOf(MainPage)).call(this, props));

    _this.state = {
      isLoaded: false,
      data: null,
      error: null
    };

    return _this;
  }

  _createClass(MainPage, [{
    key: "updateData",
    value: function updateData() {
      var _this2 = this;

      // Make an API call to retrieve the data...
      //fetch("/plugins/signalk-vanguard-plugin/api/testData")
      fetchh("http://vanguard-drone.local:3443/signalk/v1/").then(function (res) {
        var myres = res;
        return res.json();
      }).then(function (data) {
        _this2.setState({
          isLoaded: true,
          error: null,
          data: data
        });
      }, function (error) {
        _this2.setState({
          isLoaded: true,
          error: error,
          data: null
        });
      });
    }
  }, {
    key: "componentDidMount",
    value: function componentDidMount() {
      var _this3 = this;

      this.updateData();
      // Automatically update the page every 10 seconds...
      this.interval = setInterval(function () {
        return _this3.updateData();
      }, 10000);
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      clearInterval(this.interval);
    }
  }, {
    key: "render",
    value: function render() {
      var _state = this.state,
          isLoaded = _state.isLoaded,
          data = _state.data,
          error = _state.error;


      if (!isLoaded) {
        return React.createElement(
          "div",
          null,
          "Waiting for response from server..."
        );
      } else if (error) {
        return React.createElement(
          "div",
          null,
          "Error: ",
          error.message
        );
      } else {
        return React.createElement(
          "div",
          null,
          React.createElement(
            "h1",
            null,
            "Vanguard Piloting and Reporting"
          ),
          React.createElement(
            "div",
            { className: "info" },
            "GPS position: ",
            data.pos
          ),
          React.createElement(
            "div",
            { className: "info" },
            "Depth: ",
            data.depth
          ),
          React.createElement(
            "div",
            { className: "info" },
            "Speed: ",
            data.speed
          ),
          React.createElement(
            "div",
            { className: "info" },
            "Heading: ",
            data.heading
          ),
          React.createElement(
            "div",
            { className: "info" },
            "Course over ground: ",
            data.course
          ),
          React.createElement(
            "div",
            { className: "info" },
            "Closest approach (from AIS): ",
            data.closestAppr
          ),
          React.createElement(
            "div",
            { className: "info" },
            "Estimated time of arrival: ",
            data.tripETA
          ),
          React.createElement(
            "div",
            { className: "info" },
            "Water surface temp: ",
            data.waterTemp
          ),
          React.createElement(
            "div",
            { className: "info" },
            "Outside air temperature: ",
            data.outsideTemp
          ),
          React.createElement(
            "div",
            { className: "info" },
            "Outside air rel humitity: ",
            data.outsideRelHumid
          ),
          React.createElement(
            "div",
            { className: "info" },
            "Generic/example data value: ",
            data.someSKData
          )
        );
      }
    }
  }]);

  return MainPage;
}(React.Component);

var domContainer = document.querySelector('#mainBody');
ReactDOM.render(React.createElement(MainPage, null), domContainer);