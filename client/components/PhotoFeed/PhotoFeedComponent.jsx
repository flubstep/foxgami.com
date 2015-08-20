import React from 'react';
import PhotoFeedItem from 'components/PhotoFeed/PhotoFeedItem.jsx';

export default React.createClass({

  getInitialState() {
    return {
      items: [
        { 'title': 'Dog makes a bad ass leap', 'image_url': 'client/resources/clip1.jpg' },
        { 'title': 'Love in black and white', 'image_url': 'client/resources/clip2.jpg' },
        { 'title': 'Excited owls', 'image_url': 'client/resources/clip3.jpg' },
        { 'title': 'For those who wonder what a baby polar bear looks like', 'image_url': 'client/resources/clip4.jpg' },
        { 'title': 'My favorite little man', 'image_url': 'client/resources/clip5.jpg'}
      ]
    };
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