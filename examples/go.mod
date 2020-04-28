module github.com/crasiak/pulumi-grafana/examples

go 1.13

require (
	github.com/crasiak/pulumi-grafana/sdk v0.0.0-20200428230456-88ae9d04ecdc
	github.com/crasiak/terraform-provider-grafana v1.5.2 // indirect
	github.com/hashicorp/terraform-plugin-sdk v1.11.0 // indirect
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.1.1 // indirect
	github.com/pulumi/pulumi/sdk/v2 v2.1.0
)

replace (
	github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
	github.com/crasiak/pulumi-grafana/sdk => ../sdk
)
