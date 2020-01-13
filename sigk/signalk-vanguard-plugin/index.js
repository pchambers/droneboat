const Bacon = require('baconjs');
const SignalKPlugin = require('signalk-plugin-base');


class Drone extends SignalKPlugin {

  constructor(app) {
    super(app, 'signalk-vanguard-plugin', 'Vanguard Piloting and Reporting', 'Explores and maps water depth');


    this.optStr('posSKPath', 'SignalK path for GPS position', 'navigation.position');
    this.optStr('posSourceType', 'Source Type filter for GPS position', '', false, 'Leave blank for all');
    this.optStr('posSourceTalker', 'Source Talker filter for GPS position', '', false, 'Leave blank for all');

    this.optStr('depthSKPath', 'SignalK path for Depth', 'environment.depth.belowSurface');
    this.optStr('depthSourceType', 'Source Type filter for Depth', '', false, 'Leave blank for all');
    this.optStr('depthSourceTalker', 'Source Talker filter for Depth', '', false, 'Leave blank for all');

    this.optStr('speedSKPath', 'SignalK path for Speed', 'navigation.speedOverGround');
    this.optStr('speedSourceType', 'Source Type filter for Speed', '', false, 'Leave blank for all');
    this.optStr('speedSourceTalker', 'Source Talker filter for Speed', '', false, 'Leave blank for all');

    this.optStr('headingSKPath', 'SignalK path for Heading', 'navigation.headingTrue');
    this.optStr('headingSourceType', 'Source Type filter for Heading', '', false, 'Leave blank for all');
    this.optStr('headingSourceTalker', 'Source Talker filter for Heading', '', false, 'Leave blank for all');

    this.optStr('courseSKPath', 'SignalK path for Course over ground', 'navigation.courseOverGroundTrue');
    this.optStr('courseSourceType', 'Source Type filter for Course over ground', '', false, 'Leave blank for all');
    this.optStr('courseSourceTalker', 'Source Talker filter for Course over ground', '', false, 'Leave blank for all');

    this.optStr('closestApprSKPath', 'SignalK path for Closest approach (from AIS)', 'navigation.closestApproach');
    this.optStr('closestApprSourceType', 'Source Type filter for Closest approach (from AIS)', '', false, 'Leave blank for all');
    this.optStr('closestApprSourceTalker', 'Source Talker filter for Closest approach (from AIS)', '', false, 'Leave blank for all');

    this.optStr('tripETASKPath', 'SignalK path for Estimated time of arrival', 'navigation.destination.eta');
    this.optStr('tripETASourceType', 'Source Type filter for Estimated time of arrival', '', false, 'Leave blank for all');
    this.optStr('tripETASourceTalker', 'Source Talker filter for Estimated time of arrival', '', false, 'Leave blank for all');

    this.optStr('waterTempSKPath', 'SignalK path for Water surface temp', 'environment.water.temperature');
    this.optStr('waterTempSourceType', 'Source Type filter for Water surface temp', '', false, 'Leave blank for all');
    this.optStr('waterTempSourceTalker', 'Source Talker filter for Water surface temp', '', false, 'Leave blank for all');

    this.optStr('outsideTempSKPath', 'SignalK path for Outside air temperature', 'environment.outside.temperature');
    this.optStr('outsideTempSourceType', 'Source Type filter for Outside air temperature', '', false, 'Leave blank for all');
    this.optStr('outsideTempSourceTalker', 'Source Talker filter for Outside air temperature', '', false, 'Leave blank for all');

    this.optStr('outsideRelHumidSKPath', 'SignalK path for Outside air rel humitity', 'environment.outside.humidity');
    this.optStr('outsideRelHumidSourceType', 'Source Type filter for Outside air rel humitity', '', false, 'Leave blank for all');
    this.optStr('outsideRelHumidSourceTalker', 'Source Talker filter for Outside air rel humitity', '', false, 'Leave blank for all');

    this.optStr('someSKDataSKPath', 'SignalK path for Generic/example data value', 'path.to.some.value');
    this.optStr('someSKDataSourceType', 'Source Type filter for Generic/example data value', '', false, 'Leave blank for all');
    this.optStr('someSKDataSourceTalker', 'Source Talker filter for Generic/example data value', '', false, 'Leave blank for all');


  }


  // Initialization of data streams and properties are done here...
  onPluginStarted() {

          
     // This is for API demonstration only (see registerWithRouter())
     this.apiTestData = {};
     

     // BaconJS data stream for GPS position -----------------------------------------------------------------
     this.strmPos = this.getSKBus(this.options.posSKPath);

     this.strmPosVal = this.strmPos
         .filter(delta => {  return this.wildcardEq(delta
          .source.type, this.options.posSourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.posSourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmPosVal, onPosValue );

     // Uncomment this line to view incomming values on console...
     this.subscribeVal(this.strmPos, delta => { this.debug(`Pos: ${JSON.stringify(delta, null, 2)}`) } );
     this.subscribeVal(this.strmPosVal, value => { this.debug(`Pos (filtered): ${JSON.stringify(value, null, 2)}`) } );


     // BaconJS data stream for Depth -----------------------------------------------------------------
     this.strmDepth = this.getSKBus(this.options.depthSKPath);

     this.strmDepthVal = this.strmDepth
         .filter(delta => {  return this.wildcardEq(delta.source.type, this.options.depthSourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.depthSourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmDepthVal, onDepthValue );

     // Uncomment this line to view incomming values on console...
     // this.subscribeVal(this.strmDepth, delta => { this.debug(`Depth: ${JSON.stringify(delta, null, 2)}`) } );
     // this.subscribeVal(this.strmDepthVal, value => { this.debug(`Depth (filtered): ${JSON.stringify(value, null, 2)}`) } );


     // BaconJS data stream for Speed -----------------------------------------------------------------
     this.strmSpeed = this.getSKBus(this.options.speedSKPath);

     this.strmSpeedVal = this.strmSpeed
         .filter(delta => {  return this.wildcardEq(delta.source.type, this.options.speedSourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.speedSourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmSpeedVal, onSpeedValue );

     // Uncomment this line to view incomming values on console...
     // this.subscribeVal(this.strmSpeed, delta => { this.debug(`Speed: ${JSON.stringify(delta, null, 2)}`) } );
     // this.subscribeVal(this.strmSpeedVal, value => { this.debug(`Speed (filtered): ${JSON.stringify(value, null, 2)}`) } );


     // BaconJS data stream for Heading -----------------------------------------------------------------
     this.strmHeading = this.getSKBus(this.options.headingSKPath);

     this.strmHeadingVal = this.strmHeading
         .filter(delta => {  return this.wildcardEq(delta.source.type, this.options.headingSourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.headingSourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmHeadingVal, onHeadingValue );

     // Uncomment this line to view incomming values on console...
     // this.subscribeVal(this.strmHeading, delta => { this.debug(`Heading: ${JSON.stringify(delta, null, 2)}`) } );
     // this.subscribeVal(this.strmHeadingVal, value => { this.debug(`Heading (filtered): ${JSON.stringify(value, null, 2)}`) } );


     // BaconJS data stream for Course over ground -----------------------------------------------------------------
     this.strmCourse = this.getSKBus(this.options.courseSKPath);

     this.strmCourseVal = this.strmCourse
         .filter(delta => {  return this.wildcardEq(delta.source.type, this.options.courseSourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.courseSourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmCourseVal, onCourseValue );

     // Uncomment this line to view incomming values on console...
     // this.subscribeVal(this.strmCourse, delta => { this.debug(`Course: ${JSON.stringify(delta, null, 2)}`) } );
     // this.subscribeVal(this.strmCourseVal, value => { this.debug(`Course (filtered): ${JSON.stringify(value, null, 2)}`) } );


     // BaconJS data stream for Closest approach (from AIS) -----------------------------------------------------------------
     this.strmClosestAppr = this.getSKBus(this.options.closestApprSKPath);

     this.strmClosestApprVal = this.strmClosestAppr
         .filter(delta => {  return this.wildcardEq(delta.source.type, this.options.closestApprSourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.closestApprSourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmClosestApprVal, onClosestApprValue );

     // Uncomment this line to view incomming values on console...
     // this.subscribeVal(this.strmClosestAppr, delta => { this.debug(`ClosestAppr: ${JSON.stringify(delta, null, 2)}`) } );
     // this.subscribeVal(this.strmClosestApprVal, value => { this.debug(`ClosestAppr (filtered): ${JSON.stringify(value, null, 2)}`) } );


     // BaconJS data stream for Estimated time of arrival -----------------------------------------------------------------
     this.strmTripETA = this.getSKBus(this.options.tripETASKPath);

     this.strmTripETAVal = this.strmTripETA
         .filter(delta => {  return this.wildcardEq(delta.source.type, this.options.tripETASourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.tripETASourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmTripETAVal, onTripETAValue );

     // Uncomment this line to view incomming values on console...
     // this.subscribeVal(this.strmTripETA, delta => { this.debug(`TripETA: ${JSON.stringify(delta, null, 2)}`) } );
     // this.subscribeVal(this.strmTripETAVal, value => { this.debug(`TripETA (filtered): ${JSON.stringify(value, null, 2)}`) } );


     // BaconJS data stream for Water surface temp -----------------------------------------------------------------
     this.strmWaterTemp = this.getSKBus(this.options.waterTempSKPath);

     this.strmWaterTempVal = this.strmWaterTemp
         .filter(delta => {  return this.wildcardEq(delta.source.type, this.options.waterTempSourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.waterTempSourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmWaterTempVal, onWaterTempValue );

     // Uncomment this line to view incomming values on console...
     // this.subscribeVal(this.strmWaterTemp, delta => { this.debug(`WaterTemp: ${JSON.stringify(delta, null, 2)}`) } );
     // this.subscribeVal(this.strmWaterTempVal, value => { this.debug(`WaterTemp (filtered): ${JSON.stringify(value, null, 2)}`) } );


     // BaconJS data stream for Outside air temperature -----------------------------------------------------------------
     this.strmOutsideTemp = this.getSKBus(this.options.outsideTempSKPath);

     this.strmOutsideTempVal = this.strmOutsideTemp
         .filter(delta => {  return this.wildcardEq(delta.source.type, this.options.outsideTempSourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.outsideTempSourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmOutsideTempVal, onOutsideTempValue );

     // Uncomment this line to view incomming values on console...
     // this.subscribeVal(this.strmOutsideTemp, delta => { this.debug(`OutsideTemp: ${JSON.stringify(delta, null, 2)}`) } );
     // this.subscribeVal(this.strmOutsideTempVal, value => { this.debug(`OutsideTemp (filtered): ${JSON.stringify(value, null, 2)}`) } );


     // BaconJS data stream for Outside air rel humitity -----------------------------------------------------------------
     this.strmOutsideRelHumid = this.getSKBus(this.options.outsideRelHumidSKPath);

     this.strmOutsideRelHumidVal = this.strmOutsideRelHumid
         .filter(delta => {  return this.wildcardEq(delta.source.type, this.options.outsideRelHumidSourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.outsideRelHumidSourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmOutsideRelHumidVal, onOutsideRelHumidValue );

     // Uncomment this line to view incomming values on console...
     // this.subscribeVal(this.strmOutsideRelHumid, delta => { this.debug(`OutsideRelHumid: ${JSON.stringify(delta, null, 2)}`) } );
     // this.subscribeVal(this.strmOutsideRelHumidVal, value => { this.debug(`OutsideRelHumid (filtered): ${JSON.stringify(value, null, 2)}`) } );


     // BaconJS data stream for Generic/example data value -----------------------------------------------------------------
     this.strmSomeSKData = this.getSKBus(this.options.someSKDataSKPath);

     this.strmSomeSKDataVal = this.strmSomeSKData
         .filter(delta => {  return this.wildcardEq(delta.source.type, this.options.someSKDataSourceType) &&
                                    this.wildcardEq(delta.source.talker, this.options.someSKDataSourceTalker); 
                         } )
         .map(".value");

     this.subscribeVal(this.strmSomeSKDataVal, onSomeSKDataValue );

     // Uncomment this line to view incomming values on console...
     // this.subscribeVal(this.strmSomeSKData, delta => { this.debug(`SomeSKData: ${JSON.stringify(delta, null, 2)}`) } );
     // this.subscribeVal(this.strmSomeSKDataVal, value => { this.debug(`SomeSKData (filtered): ${JSON.stringify(value, null, 2)}`) } );


  }


  onPluginStopped() {
     // Here is where you clean up things done in onPluginStarted() OTHER THAN
     // subscriptions created by calling subscribeVal() (those are cleaned up
     // automatically).
  }



  /**
   * This is where RESTul API call responses are defined...
   * @param {object} router An ExpressJS "Router" object
   * @see https://expressjs.com/en/guide/routing.html
   */
  registerWithRouter(router) {

    this.debug("Registering routes...");
    router.get("/api/testData", (req, res) => {
        if (this.running) {
          let jReturnVal = this.apiTestData;
          this.debug(`Returning JSON value ${JSON.stringify(jReturnVal)}`)
          res.json(jReturnVal);
        }
        else {
          res.status(503).send('Plugin not running');
        }
    });
  }




   onPosValue(pos) {
      // Handle changes to GPS position here

      // For API demo purposes only:
      this.apiTestData.pos = pos;
   }


   onDepthValue(depth) {
      // Handle changes to Depth here

      // For API demo purposes only:
      this.apiTestData.depth = depth;
   }


   onSpeedValue(speed) {
      // Handle changes to Speed here

      // For API demo purposes only:
      this.apiTestData.speed = speed;
   }


   onHeadingValue(heading) {
      // Handle changes to Heading here

      // For API demo purposes only:
      this.apiTestData.heading = heading;
   }


   onCourseValue(course) {
      // Handle changes to Course over ground here

      // For API demo purposes only:
      this.apiTestData.course = course;
   }


   onClosestApprValue(closestAppr) {
      // Handle changes to Closest approach (from AIS) here

      // For API demo purposes only:
      this.apiTestData.closestAppr = closestAppr;
   }


   onTripETAValue(tripETA) {
      // Handle changes to Estimated time of arrival here

      // For API demo purposes only:
      this.apiTestData.tripETA = tripETA;
   }


   onWaterTempValue(waterTemp) {
      // Handle changes to Water surface temp here

      // For API demo purposes only:
      this.apiTestData.waterTemp = waterTemp;
   }


   onOutsideTempValue(outsideTemp) {
      // Handle changes to Outside air temperature here

      // For API demo purposes only:
      this.apiTestData.outsideTemp = outsideTemp;
   }


   onOutsideRelHumidValue(outsideRelHumid) {
      // Handle changes to Outside air rel humitity here

      // For API demo purposes only:
      this.apiTestData.outsideRelHumid = outsideRelHumid;
   }







};


module.exports = function (app) {
  var plugin = new Drone(app);
  return plugin;
}