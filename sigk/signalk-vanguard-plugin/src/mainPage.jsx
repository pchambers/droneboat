'use strict';

class MainPage extends React.Component {

      constructor(props) {
          super(props);

          // Setup the React "state" object used by this page...
          this.state = {
            isLoaded: false,
            data: null,
            error: null,
        };

      }
    
      updateData() {
        // Make an API call to retrieve the data...
        fetch("/plugins/signalk-vanguard-plugin/api/testData")
          .then((res) => {
             let myres = res;
             return res.json()
          })
          .then(
            (data) => {
              this.setState({
                isLoaded: true,
                error: null,
                data,
              });
            },
            (error) => {
              this.setState({
                isLoaded: true,
                error,
                data: null
              });
            }
          )
      }


      componentDidMount() {
        this.updateData();
        // Automatically update the page every 10 seconds...
        this.interval = setInterval(() => this.updateData(), 10000);        
      }
    

      componentWillUnmount() {
        clearInterval(this.interval);
      }


      render() {
        const { isLoaded, data, error } = this.state;

        if (!isLoaded) {
          return <div>Waiting for response from server...</div>;
        }
        else if (error) {
          return <div>Error: {error.message}</div>;
        } 
        else {
          return (
            <div>
              <h1>Vanguard Piloting and Reporting</h1>
              <div className="info">GPS position: {data.pos}</div>
              <div className="info">Depth: {data.depth}</div>
              <div className="info">Speed: {data.speed}</div>
              <div className="info">Heading: {data.heading}</div>
              <div className="info">Course over ground: {data.course}</div>
              <div className="info">Closest approach (from AIS): {data.closestAppr}</div>
              <div className="info">Estimated time of arrival: {data.tripETA}</div>
              <div className="info">Water surface temp: {data.waterTemp}</div>
              <div className="info">Outside air temperature: {data.outsideTemp}</div>
              <div className="info">Outside air rel humitity: {data.outsideRelHumid}</div>
              <div className="info">Generic/example data value: {data.someSKData}</div>
            </div>
          );
        }
      }
}

let domContainer = document.querySelector('#mainBody');
ReactDOM.render(<MainPage />, domContainer);
