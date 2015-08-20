import React from 'react';

export default React.createClass({

  getInitialState() {
    return {
      comments: [
        { user_name: 'janlaureys9', text: 'Just put him in the water, but be careful because he might shrink.', replies: 40},
        { user_name: 'tinyneko', text: "I don't normally post in /r/aww, but this is so damn cute that I squealed very loudly at work and scared my coworker. I just want to hug it and squeeze it and brush the sand off its little paws and nose and oh my god it's so cute I might implode.", replies: 24},
        { user_name: 'need2getaclue', text: 'I LOVE COCAINE!!', replies: 3}
      ]
    };
  },

  render() {
    return (
    	<section className='comment-feed padding-16 story-section'>
        <h2 className="medium">Comments ({this.state.comments.length})</h2>
    	  {this.state.comments.map((comment, index) => {
        	return <section>
            <p className='username medium'>{comment.user_name}</p>
            <p className='comment-text medium'>{comment.text}</p>
            <p className='textbox xx-small'>{comment.replies} replies</p>
          </section>
        })}
    	</section>
    );
  }
});