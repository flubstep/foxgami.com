'use strict';

import 'styles/main.scss';

import React from 'react/addons';
import IndexComponent from 'components/Index/IndexComponent.jsx';
import BrowseComponent from 'components/Browse/BrowseComponent.jsx';
import StoryPageComponent from 'components/StoryPage/StoryPageComponent.jsx';
import Router from 'react-router';
import {Route, DefaultRoute, Link, RouteHandler} from 'react-router';

var App = React.createClass({
  render() {
    return (
      <div className="nav">
        <RouteHandler />
      </div>
    );
  }
});

var routes = (
  <Route name="app" path="/" handler={App}>
    <DefaultRoute handler={BrowseComponent} />
    <Route name="item" path="item/:storyId" handler={StoryPageComponent} />
  </Route>
);

Router.run(routes, ((Handler) => {
  React.render(<Handler/>, document.body);
}));