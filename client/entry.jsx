'use strict';

import 'styles/main.scss';

import React from 'react/addons';
import IndexComponent from 'components/Index/IndexComponent.jsx';
import BrowseComponent from 'components/Browse/BrowseComponent.jsx';
import StoryPageComponent from 'components/StoryPage/StoryPageComponent.jsx';
import {Route, DefaultRoute, run} from 'react-router';

var messages = [
  "HELLO ALBERT!",
  "This is kathy.",
  "Who knows what you'll find at FOXGAMI?",
  "Meaning, FOXGAMI is just a domain name and logo mark right now.",
  "Maybe it will have games?",
  "Maybe it will have cute art?",
  "Maybe just a cute learning experience?",
  "*shrug*",
  "PS I like foxes ^_^"
];

if (document.location.pathname.substring(0, 5) == '/item') {
  React.render(<StoryPageComponent />, document.body);
} else {
  React.render(<BrowseComponent />, document.body);
}