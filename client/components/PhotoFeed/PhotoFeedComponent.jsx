import React from 'react';
import PhotoFeedItem from 'components/PhotoFeed/PhotoFeedItem.jsx';

var BASE_URL = 'http://foxgami.com/api';

export default React.createClass({

  getInitialState() {
    return { items: [] };
  },

  componentDidMount() {
    fetch(BASE_URL + '/stories').then((results) => {
      this.setState({ items: JSON.parse(results) });
    });
  },

  render() {
    return (
    	<section className='photo-feed'>
    	  {this.state.items.map((item, index) => {
        	return <PhotoFeedItem item={item} />
        })}
    	</section>
    );
  }
});