import React from 'react';

import Box from 'grommet/components/Box';
import Label from 'grommet/components/Label';

class HomePage extends React.Component {
    render() {
        return(
            <Box flex={true} align="center">
              <Label>Welcome!</Label>
            </Box>
        )
    }
}

export default HomePage;
