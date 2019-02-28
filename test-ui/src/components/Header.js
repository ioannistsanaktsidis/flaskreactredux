import React from 'react';

import Box from 'grommet/components/Box';
import Header from 'grommet/components/Header';
import Anchor from 'grommet/components/Anchor';
import Label from 'grommet/components/Label';

const TestHeader = () => {     
  return(
   <Header pad="small" colorIndex="brand">
      <Box justify="between" direction="row" flex={true}>
        <Box flex={true}>
          <Anchor path="/">
            <Label margin="none">Test App
            </Label>
          </Anchor>
        </Box>
      </Box>
  </Header>
  )
}

export default TestHeader;
