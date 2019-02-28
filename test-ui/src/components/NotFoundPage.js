import React from 'react';
import { Link } from 'react-router-dom';
import Box from 'grommet/components/Box';

const NotFoundPage = () => {
  return (
    <Box>
      <h4>
        404 Page Not Found
      </h4>
      <Link to="/"> Go back to homepage </Link>
    </Box>
  );
};

export default NotFoundPage;
