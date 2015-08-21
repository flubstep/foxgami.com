import React from 'react';
import PhotoFeedItem from 'components/PhotoFeed/PhotoFeedItem.jsx';

var BASE_URL = 'http://www.foxgami.com/api';

export default React.createClass({

  getInitialState() {
    return { items: [] };
  },

  componentDidMount() {
    fetch(BASE_URL + '/stories').then((response) => {
      return response.json();
    }).then((results) => {
      this.setState({ items: results });
    }).catch((error) => {
      // TODO: Show an error on the page.
      console.error("Error caught fetching stories:", error);
    });
  },

  render() {
    return (
    	<section className='photo-feed outer'>
    	  {this.state.items.map((item, index) => {
        	return <PhotoFeedItem item={item} />
        })}
    	</section>
    );
  }
});