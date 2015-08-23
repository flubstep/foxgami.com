import React from 'react';
import {Link} from 'react-router';

export default React.createClass({

  render() {
    return (
      <section className="button elliptical small flex-centered-xy">
        <Link to="app">
          HOME
        </Link>
      </section>
    );
  }

})