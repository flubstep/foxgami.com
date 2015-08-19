import React from 'react';

export default React.createClass({

  render() {
    return (
    	<section className='item story-photo'>
        <a href="/item"><img src={this.props.item.image_url} /></a>
        <p className="textbox medium">{this.props.item.title}</p>
        <p className="x-small">posted 5 hours ago</p>
    	</section>
    );
  }
});