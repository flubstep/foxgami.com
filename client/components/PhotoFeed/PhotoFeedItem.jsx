import React from 'react';
import timeago from 'timeago';

export default React.createClass({

  render() {
    var story_date = new Date(this.props.item.submitted_at);
    var story_timeago = timeago(story_date);
    return (
    	<section className='item story-photo'>
        <a href="/item"><img src={this.props.item.image_url} /></a>
        <p className="textbox medium">{this.props.item.title}</p>
        <p className="x-small">posted {story_timeago}</p>
    	</section>
    );
  }
});