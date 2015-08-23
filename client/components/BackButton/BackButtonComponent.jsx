import React from 'react';
import {Link} from 'react-router';

export default React.createClass({

  render() {
    return (
      <section className="nav elliptical small flex-centered-xy">
        <Link to="app">
          HOME
        </Link>
      </section>
    );
  }

})