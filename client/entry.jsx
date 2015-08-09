'use strict';

import 'styles/main.scss';

import React from 'react/addons';
import IndexComponent from 'components/Index/IndexComponent.jsx';

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

React.render(<IndexComponent items={messages}/>, document.body);
