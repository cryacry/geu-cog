package config

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestDockerImageName(t *testing.T) {
	require.Equal(t, "geu_cog-foo", DockerImageName("/home/joe/foo"))
	require.Equal(t, "geu_cog-foo", DockerImageName("/home/joe/Foo"))
	require.Equal(t, "geu_cog-foo", DockerImageName("/home/joe/geu_cog-foo"))
	require.Equal(t, "geu_cog-my-great-model", DockerImageName("/home/joe/my great model"))
	require.Equal(t, 30, len(DockerImageName("/home/joe/verylongverylongverylongverylongverylongverylongverylong")))
}
