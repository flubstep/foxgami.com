import React from 'react';
import PhotoFeedItem from 'components/PhotoFeed/PhotoFeedItem.jsx';
import foxgamiApi from 'helpers/foxgamiApi.jsx';

export default React.createClass({

  getInitialState() {
    return { items: [] };
  },

  componentDidMount() {
    foxgamiApi.get('/stories').then((results) => {
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